from bs4 import BeautifulSoup
import requests
import re
from openpyxl import Workbook

class FermosaExtracter:
    """ This Class extract the plant data from Fermosa plant website 
    and stores that data into an excel file.
    """
    def __init__(self, url, pages):
        self.result = []
        self.totalpages = pages
        self.url = url
        self.__scrap()          # Call the function to get the data from the website

    def makeData(self, link, plant_type, name, price, variegated):
        # Fetches the specific plant details from its product page

        try:
            data = requests.get(link).text
            temp = BeautifulSoup(data, "html.parser").find("div", class_="pd_summary").p.text
            pattern = re.compile(r"\d\.\s*[ a-zA-Z]*", flags=re.I)
            match = pattern.findall(temp)
            
            tempdict = {"URL": link, "Type": plant_type, "Price": price, "Number": 1, "Variegated": variegated, "Name1": name}
            
            if plant_type == "combo":
                for i, entry in enumerate(match, start=1):

                    tempdict[f"Name{i}"] = entry.split(".")[1]

                    if "Comes" in tempdict[f"Name{i}"]:
                        tempdict[f"Name{i}"]=tempdict[f"Name{i}"].split("Comes")[0].strip()
                    elif "Images" in tempdict[f"Name{i}"]:
                        tempdict[f"Name{i}"]=tempdict[f"Name{i}"].split("Images")[0].strip()
                
                tempdict["Number"] = len(match)
        
            return tempdict         # returning the dictionary having plants details
        
        except Exception as e:
            print(f"Error: {e}")
            return None

    def __scrap(self):
        # Fetches the plants details from the multiple pages of Fermosa website
        try:
            pageno = 1
            while pageno <= self.totalpages:
                temp = requests.get(f"{self.url}?page={pageno}").text
                soup = BeautifulSoup(temp, 'html.parser').find_all("div", class_="product-item-v5")
                
                for i in soup:
                    variegated = "NO"
                    upper = i.div
                    link = "https://fermosaplants.com" + upper.h4.a.get("href")
                    name = upper.h4.a.string.strip()
                    plant_type = "Uncategorized"
                    
                    if "combo" in name.lower():
                        plant_type = "combo"
                    elif "clump" in name.lower():
                        plant_type = "clump"
                    elif "leaf" in name.lower():
                        plant_type = "leaf"
                    elif "plant" in name.lower():
                        plant_type = "plant" 
                    elif "pub" in name.lower():
                        plant_type = "pub"
                    
                    if "combo" not in name.lower():
                        variegated = "YES" if "variegated" in name.lower() else "NO"
                    
                    price = upper.find("p", class_="price-product mb-0").span.string.strip()
                    plant_data = self.makeData(link, plant_type, name, price, variegated)
                    
                    if plant_data:
                        self.result.append(plant_data)
                
                pageno += 1
        except Exception as e:
            print(e)
    
    def saveDataToExcel(self, filename="result.xlsx"):
        # Stores the fetched data into excel file 
        wb = Workbook()
        ws = wb.active
        if not self.result:
            print("No data to save.")
            return

        # It gives record that have maximum number of details
        max_length_row = max(self.result, key=len)
        headers = list(max_length_row.keys())
        ws.append(headers)
        
        for data in self.result:
            row = [data.get(header, "") for header in headers]
            ws.append(row)
        wb.save(filename)

obj = FermosaExtracter("https://fermosaplants.com/collections/sansevieria", 8)
obj.saveDataToExcel("fermosa_data.xlsx")