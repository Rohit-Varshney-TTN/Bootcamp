dict1={}
str="""Python Multiline String Using Triple-Quotes.
Using the triple quotes style is one of the easiest and most common ways to split a large string into a multiline Python string. Triple quotes (''' or \""") can be used to create 
a multiline string. It allows you to format text over many lines and include line breaks. Put two triple quotes around the multiline Python string, one at the start and one at 
the end, to define it."""
str=str.split()
for i in str:
    if i in dict1.keys():
        dict1[i]+=1
    else:
        dict1[i]=1
print("Word\t","Length\t","Occurrence")
for key , value in dict1.items():
    if value>1:
        print(key,"\t",len(key),"\t",value)