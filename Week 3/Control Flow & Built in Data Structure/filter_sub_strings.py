str="I have an input string which contains even and odd numbers of vowels aA aa aaa ae aeo"
str=str.split()
vowels=['a','e','i','o','u']
for i in range(len(str)):
    count=0
    for char in str[i]:
        if char.lower() in vowels :
            count+=1
    if count%2==0:
        print(str[i])