# python program to create a simple calculator

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1+num2)/2
# user input
print("select an operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Average")

select=int(input("select a operation from 1,2,3,4,5: "))
num1=int(input("enter 1 number: "))
num2=int(input("enter 2 number: "))

if select==1:
   print(num1,"+",num2,"=",add(num1,num2))
elif select==2:
   print(num1,"-",num2,"=",sub(num1,num2))
elif select==3:
   print(num1,"*",num2,"=",multiply(num1,num2))
elif select==4:
   print(num1,"/",num2,"=",divide(num1,num2))
elif select==5:
   print("(",num1,"+",num2,")","/","2","=",avg(num1,num2))
else:
    print("invalid operation")                