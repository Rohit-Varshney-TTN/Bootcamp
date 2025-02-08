def is_prime(n):
    if n<=1:
        return False
    else :
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

n=int(input("Enter the number to check whether it is prime or not :"))
if is_prime(n):
    print(n ,"is a prime number.")
else :
    print(n ,"is not a prime number.")
        
    