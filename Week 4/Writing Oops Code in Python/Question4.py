class MathOperations:
    def add(self,a,b,c=None):
        if c is None:
            return a+b
        return a+b+c

obj=MathOperations()
print(obj.add(4,2))
print(obj.add(4,3,3))