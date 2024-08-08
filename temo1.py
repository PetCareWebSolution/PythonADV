# Operator Overloading: >

class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        
        if self.age > other.age:

            return True
        
        else:

            return False
        


p1=person("Royal",57)

p2=person("Shyam",78)


if p1>p2:
    print(f"{p1.name} will be pay the bill")

else:

     print(f"{p2.name} will be pay the bill")