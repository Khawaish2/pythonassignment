# question24
def add(x,y):
    t = x + y
    print(t)

def subtract(x,y):
    z  = x - y
    print(z)

def multiply(x,y):
    f = x*y
    print(f)
def divide(x,y):
    g = x/y
    print(g)
print("select one operator:")
print("1.add,2.subtract,3.multiply,4.divide")

op = int(input("select 1,2,3,4"))

num1 = int(input("enter the number 1 :"))
num2 = int(input("enter the number 2 : "))

if op == 1 :
    print(num1,"+",num2 ,"=")
    add(num1,num2)

elif op == 2 :
    print(num1,"-",num2 ,"=")
    subtract(num1,num2)

elif op == 3 :
    print(num1,"*",num2,"=")
    multiply(num1,num2)

elif op == 4 :
    print(num1 ,"/",num2,"=")
    divide(num1,num2)

else :
    print("invalid data")

