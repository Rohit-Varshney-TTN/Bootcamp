dict1 = {'Java':9, 'Python':10, 'MySQL':10,'AWS':9}
print("Before Sorting : ",dict1)

Keys = list(dict1.keys())
Keys.sort()

sorted_dict={}
for i in Keys:
    sorted_dict[i]=dict1[i]
print("The sorted dictionary : ",sorted_dict)
