'''
Write an object oriented code to implement Prime number class.

Implement a Prime class which should have following functionality:

- Ability to test if a number is prime or not.
- Generate prime numbers
- Generate prime numbers greater than a number N
- Generate prime numbers  less than a number N
- Generate all prime numbers between N to M
- Implement __len__() to tell number of primes between N and M where N < M
- Overload +, += operators to generate prime number with respect to current prime number
- Implement __repr__() and __str__() methods

'''

class Prime:
    def __init__(self, num=2):
        self.num = num

    #checking whether the number is prime or not
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    #function to generate prime numbers
    def generate_primes(self, x):
        for n in range(2, x+1):
            if self.is_prime(n):
                yield n

    #function to generate prime number greater than n
    def primes_greater_than(self, n, count=None):
        num = n+1
        while count is None or count > 0:
            if self.is_prime(num):
                yield num
                if count is not None:
                    count -= 1
            num += 1
    
    #function to generate number less than n
    def primes_less_than(self, n):
        for num in range(2, n):
            if self.is_prime(num):
                yield num
    
    #function to generate prime number in between n and m
    def primes_between(self, n, m):
        for num in range(n, m + 1):
            if self.is_prime(num):
                yield num

    #function to count the prime number betwen n and m
    def __len__(self):
        count = 0
        for prime in self.primes_between(self.num, self.num + 100):
            count += 1
        return count
    
    #function to overload "+" operator to generate prime number w.r.t to current prime number
    def __add__(self,other):
        prime_generator = self.primes_greater_than(self.num)
        for k in range(other):
            new_prime = next(prime_generator)
        return new_prime
    
    #function to overload "+=" to generate prime number w.r.t to current prime number
    def __iadd__(self, other):
        prime_generator = self.primes_greater_than(self.num)
        for k in range(other):
            self.num = next(prime_generator)
        return self

    #function to  override the __str__()
    def __str__(self):
        return f"Prime: ({self.num})"

    #function to override the __repr()
    def __repr__(self):
        return f"Prime({self.num})"

#creating the object
p = Prime(11)
print(p.is_prime(11))
print(p + 1)
print(p + 2) 
p += 3
print(p)
print(p.__repr__())
print(list(p.primes_less_than(10)))
print(list(p.primes_greater_than(10, 5))) 
print(list(p.primes_between(10, 30)))