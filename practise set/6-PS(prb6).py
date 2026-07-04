# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try
# changing self to “slf” or “harry” and see the effects

class employee:
    def __init__(slf,name,language,salary):
        slf.name=name
        slf.language=language
        slf.salary=salary
        print("object is created")

name=employee("prajwal","python",10000)
print(name.name)
print(name.language)
print(name.salary)
print(name)
print(id(name))


#nothing happens but self is better 
#self to slf no changes the program run correctly