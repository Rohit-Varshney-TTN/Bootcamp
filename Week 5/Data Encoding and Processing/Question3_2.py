import csv
import json
# Function that convert json file to csv file
def json_to_csv():
    with open('emp.json', 'r') as file:
        header = []
        with open('user.csv', 'w') as f:
            data = json.load(file)
            # Sets the header row of csv file
            header = data[0].keys()
            csvwriter = csv.DictWriter(f, fieldnames = header,delimiter='|')
            csvwriter.writeheader()
            csvwriter.writerows(data)
json_to_csv()