import json
with open("Python_script.py","r") as file:
    dict1={"package":set(),"function":[],"class":[],"variable":set()}
    for line in file:
        line=line.strip()
        if not line:
            continue

        words=line.replace(":","").replace(","," ").split()

        if words[0]=="import" or words[0]=="from":
            dict1["package"].add(words[1].split('.')[0])
            
        elif words[0]=="def":
            dict1["function"].append(words[1])
        elif words[0]=="class":
            dict1["class"].append(words[1])
        elif "=" in words:
            for i in words[:words.index("=")]:
                if i and i.isidentifier():
                    dict1["variable"].add(i)

dict1["package"]=list(dict1["package"])
dict1["variable"]=list(dict1["variable"])

print(json.dumps(dict1,indent=4))