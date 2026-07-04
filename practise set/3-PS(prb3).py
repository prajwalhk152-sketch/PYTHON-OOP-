# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using 
# ‘object.a = 0ʼ. Does this change the class attribute?

class employee:
    a=10
b=employee()
print(b.a)
b.a=0
print(employee.a)
print(b.a)




# NO it doesnt change the object of the class 