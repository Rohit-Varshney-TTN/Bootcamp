import os 
import sys
from math import sqrt
class TTN:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print("Hello",self.name)
        print("Age:",self.age)

obj = TTN("Rohit Varshney",21)
obj.hello()

def square_root(num):
    x = sqrt(num)
    print(x)

square_root(144)