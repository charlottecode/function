def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)


choice=int(input("select 1 for addition,2 for substraction,3 for multiplication,4 for division"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))


if choice==1:
    print("addition is",add(num1,num2))

elif choice==2:
    print("substraction is",sub(num1,num2))

elif choice==3:
    print("multiplication is",mul(num1,num2))

elif choice==4:
    print("division is",div(num1,num2))

else:
    print("input is invalid")

