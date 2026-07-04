#self parameter is a reference to the current instance of the class and is used to access the attributes and methods of the class

class employee:
    name="prajwal"
    language="python"
    salary=10000

    def greet(self):
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

employee.greet(prajwal)   #this is how we can call a method of a class
employee.getinfo(prajwal)   #this is how we can call a method of a class

