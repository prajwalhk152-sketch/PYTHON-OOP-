# object oriented programing 
# class is a blueprint for creating objects

# basic class program
class employee:
    # class variable
    # attribute of a class is called class variable
    # name="prajwal"
    language="python"
    salary=10000
prajwal=employee()
prajwal.name="prajwal"   #this is instance variable
rohan=employee()
rohan.name="rohan"   #this is instance variable
print("name of an employee:", prajwal.name)
print("language:", prajwal.language)
print("salary:", prajwal.salary)

print("name of an employee:", rohan.name)
print("language:", rohan.language)
print("salary:", rohan.salary)

# here name is an instance variable and language and salary are class variables
# object is an instance of a class
