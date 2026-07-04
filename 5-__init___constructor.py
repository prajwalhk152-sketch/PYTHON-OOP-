# init constructor is a special method in python which is used to initialize the object of a class. 
# It is called when an object is created. It is defined using the __init__() method.


class employee:
    name="prajwal"
    language="python"
    salary=10000

    def __init__(self,):   #this is how we can define a constructor  dunder method 
        print("object is created")
    
    def __init__(self, name, language, salary):   #this is how we can define a constructor  dunder method
        self.name=name
        self.language=language
        self.salary=salary
        print("object is created")


    def greet(self):
        print("\nGood morning\n")

    def getinfo(self):
        print("name of an employee:", self.name)
        print("language:", self.language)
        print("salary:", self.salary)
    

prajwal=employee("prajwal H K", "js", 15000) #this is how we can create an object of a class and pass the values to the constructor
print("name of an employee:", prajwal.name)
print("language:", prajwal.language)
print("salary:", prajwal.salary)

employee.greet(prajwal)  
employee.getinfo(prajwal)  