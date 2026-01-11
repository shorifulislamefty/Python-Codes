def sum(a,b):
    result=a+b
    print('Result:',result)

def sub(a,b):
    result=a-b
    print('Result:',result)    

def multi(a,b):
    result=a*b
    print('Result:',result)

def devided(a,b):
    if b==0:
       print("Invalid input")
       return
    result=a/b
    print('Result:',result)

def reminder(a,b):
    result=a%b
    print('Result:',result)

print("===Choice your operator===")
print("1.Sumation")
print("2.Subtraction")
print("3.Multiplication")
print("4.Devided")
print("5.Reminder")
print("6.Off")
while True:
    choice=int(input("Enter your Choice:"))
    if choice==1:
        a=int(input("Enter 1st value:"))
        b=int(input("Enter 2nd value:"))
        sum(a,b)
    elif choice==2:
        a=int(input("Enter 1st value:"))
        b=int(input("Enter 2nd value:"))
        sub(a,b)
    elif choice==3:
        a=int(input("Enter 1st value:"))
        b=int(input("Enter 2nd value:"))
        multi(a,b) 
    elif choice==4:
        a=int(input("Enter 1st value:"))
        b=int(input("Enter 2nd value:"))
        devided(a,b)
    elif choice==5:
        a=int(input("Enter 1st value:"))
        b=int(input("Enter 2nd value:"))
        reminder(a,b)
    elif choice==6:
        print("Close")
        break      
    else:
        print('Please Enter valid value') 