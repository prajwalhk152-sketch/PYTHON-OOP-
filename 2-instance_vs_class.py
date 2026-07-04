class employee:
    name="prajwal"   #this is instance variable
    language="python"
    salary=10000
    def greet(self):
        print("\nGood morning\n")

prajwal=employee()
prajwal.language="java"
prajwal.salary=15000
prajwal.greet()
print("name of an employee:", prajwal.name)
print("language:", prajwal.language)
print("salary:", prajwal.salary)

# here name is an instance variable and language and salary are class variables
# object is an instance of a class