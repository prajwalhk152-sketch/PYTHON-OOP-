# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft

class programmer:
    company="Microsoft"
    
    @staticmethod
    def greet():
        print("\nGood morning\n")


    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
p1=programmer("prajwal",10000,"python")
p2=programmer("harry",10000,"python,java")
programmer.greet()
print(p1.name,p1.language,p1.salary)
print(p2.name,p2.language,p2.salary)