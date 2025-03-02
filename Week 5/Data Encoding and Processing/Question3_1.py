import csv
import json
# Function to convert csv file to json file 
def csv_to_json():
    with open('username.csv', 'r') as f:
        data = csv.DictReader(f,delimiter=';')
        with open('user.json', 'w') as j:
            # Traverse through each row in csv file
            for row in data :
                # convert the row to JSON format
                json.dump(row,j)
                j.write("\n")
csv_to_json()