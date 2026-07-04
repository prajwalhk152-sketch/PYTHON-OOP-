#static method is a method that belongs to the class rather than an instance of the class. 
# It can be called on the class itself, without creating an instance of the class. 
# Static methods are defined using the @staticmethod decorator.

class employee:
    name="prajwal"
    language="python"
    salary=10000

    @staticmethod  #this is how we can define a static method
    def greet():
        print("\nGood morning\n")

    def getinfo(self):
        print("name of an employee:", self.name)
        print("language:", self.language)
        print("salary:", self.salary)
    

prajwal=employee()
prajwal.language="java"
prajwal.salary=15000
print("name of an employee:", prajwal.name)
print("language:", prajwal.language)
print("salary:", prajwal.salary)

employee.greet()   #this is how we can call a static method of a class
employee.getinfo(prajwal)   #this is how we can call a method of a class