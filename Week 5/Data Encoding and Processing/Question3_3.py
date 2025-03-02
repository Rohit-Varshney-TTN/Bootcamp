from io import StringIO

# Function that converts
def dict_to_csv(dict1):
    # create StringIO object
    result = StringIO()
    result.write(",".join(dict1.keys()) + "\n")
    result.write(",".join(map(str,dict1.values())) + "\n")
    return result.getvalue()

dict1 = {"Name":"Rohit Varshney", "Company":"To The New","Address":"Noida","Age":21}
print(dict_to_csv(dict1))
