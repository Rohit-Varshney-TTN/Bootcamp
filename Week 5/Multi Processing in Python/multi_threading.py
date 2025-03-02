import requests
import json
import threading
import time

class NPIRegistry:
    """ This class retrieves the data from the NPI Registry site 
    and stores it into a JSON file.
    """
    
    def __init__(self, file, jsonfile):
        self.file = file
        self.jsonfile = jsonfile
        self.lock = threading.Lock()
        self.datas = []             # List to store NPI data
        self._extract_data()        # Call this function to fetch and and storing the NPI data

    def fetch_npi_data(self,npi):
        """ Fetch the NPI data using GET request 
        and stores it in a JSON file
        """

        try:
            url = f"https://npiregistry.cms.hhs.gov/api/?number={npi}&version=2.1"
            response = requests.get(url)
                
            if response.status_code == 200:
                print(f"Successfully get the data for NPI {npi}")
            else:
                print(f"Failed to get the data for NPI {npi}, Status Code: {response.status_code}")
                return
                
            data = response.json()
                
            if "results" not in data:
                print(f"No data exists for NPI {npi}")
                return

            result = data["results"][0]
                
            # Stores the NPI details for the numbers
            record = {
                    "Number": result.get("number", ""),
                    "Enumeration Date": result.get("basic", {}).get("enumeration_date", ""),
                    "NPI Type": result.get("enumeration_type", ""),
                    "Sole Proprietor": result.get("basic", {}).get("sole_proprietor", ""),
                    "Status": "Active" if result.get("basic", {}).get("status") == "A" else "Inactive",
                    "Addresses": {
                        "Mailing Address": {},
                        "Primary Practice Address": {}
                    },
                    "Taxonomies": result.get("taxonomies", [])
                }

            # Fetch the address details
            for address in result.get("addresses", []):
                address_type = address.get("address_purpose", "").lower()
                address_data = {
                        "Street-1": address.get("address_1", ""),
                        "Street-2": address.get("address_2", ""),
                        "City": address.get("city", ""),
                        "State": address.get("state", ""),
                        "Zip": address.get("postal_code", ""),
                        "Phone": address.get("telephone_number", ""),
                        "Fax": address.get("fax_number", "")
                    }
                    
                if "mailing" in address_type:
                    record["Addresses"]["Mailing Address"] = address_data
                elif "Practice" in address_type:
                    record["Addresses"]["Primary Practice Address"] = address_data
                else:
                    if not record["Addresses"]["Primary Practice Address"]:
                        record["Addresses"]["Primary Practice Address"] = address_data

            # To ensure that the data is added with thread-safe 
            with self.lock:
                self.datas.append(record)

        except Exception as e:
            print(f"Error for NPI {npi}: {e}")
                
    def _extract_data(self):
        with open(self.file, 'r') as f:
            npi_list = [line.strip('\n"') for line in f]

        t1=time.time()
            
        threads=[]
        for npi in npi_list:
            thread=threading.Thread(target=self.fetch_npi_data,args=(npi,))
            thread.start()
            threads.append(thread)
        
        # Halt the main thread's execution 
        for i in threads:
            i.join()

        # Write the fetched NPI data to json file
        with open(self.jsonfile, "w") as jf:
            json.dump(self.datas, jf, indent=5)

        t2=time.time()
        print("Time Taken = ",t2-t1)
                
obj = NPIRegistry("npi_number.txt", "data.json")