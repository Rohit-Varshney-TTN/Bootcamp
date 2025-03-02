def binary_rep(n):
    binary=""
    if n==0:
        return 0
    else:
        while(n>0):
            binary=binary+str(n%2)
            n=n//2
    return binary[::-1]

def octal_rep(n):
    octal=""
    if n==0:
        return 0
    else:
        while(n>0):
            octal=octal+str(n%8)
            n=n//8
    return octal[::-1]

def hexa_decimal_rep(n):
    hexa="0123456789ABCDEF"
    hexa_decimal=""
    if n==0:
        return 0
    else:
        while(n>0):
            hexa_decimal=hexa_decimal+hexa[n%16]
            n=n//16
    return hexa_decimal[::-1]

n=int(input("Enter the number :"))
print("The binary representation of a ",n,"is :" ,binary_rep(n))
print("The octal representation of a ",n,"is :" ,octal_rep(n))
print("The hexa decimal representation of a ",n,"is :" ,hexa_decimal_rep(n))