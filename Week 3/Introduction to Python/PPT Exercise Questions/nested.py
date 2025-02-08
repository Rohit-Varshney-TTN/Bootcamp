list3 = [1,2,[3,4,'hello']]
print("Before replacement : ",list3)
# Reassign the "hello" in nested list to say "goodbye" instead :
list3[2][2]="goodbye"
print("After replacement : ",list3)

