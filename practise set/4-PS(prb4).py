# 4. Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self,num):
        self.num=num
    
    @staticmethod
    def greet():
        print("\n Hello \n")
    
    def square(self):
        print(f"the square of {self.num} is : {self.num*self.num}")
    
    def cube(self):
        print(f"the cube of {self.num} is : {self.num**3}")

    def square_root(self):
        print(f"the square root of {self.num} is {self.num**0.5} ")
num=int(input("Enetr the number to find the square,cube and square root of the number : "))
a=calculator(num)    
a.square()
a.cube()
a.square_root()