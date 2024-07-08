# looping statement

# elif
# print("enter number")
# num=int (input("entr number"))
# if(num>0):
#     print("positive")
# elif(num<0):
#     print("negative")
# else:
#     print("zero")
# function
# def function name (parameter)
# def sum(a,b):
#     c=a+b
#     print("sum is:",c)
# sum(2,3)
# sum(int(input()),int(input()))

# concept of oop
# class collection of dataset and function
# class calc:
#     def sum(self,a,b):
#         return (a+b)
#     def mul(self,a,b):
#         return (a*b)
# q=calc()
# print(q.sum(2,3))
# print(q.mul(2,3))

# constructor
class std:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_std_details(self):
        print("student name::",self.name)
        print("student id::",self.id)
s1=std("ram",1)
s2=std("hari",2)
s1.print_std_details()
s2.print_std_details()
