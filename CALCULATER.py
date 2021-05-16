print("*****WELCOME TO MY FIRST CALCULATER PROGRAM*****",
      "\nCHOOSE YOUR CALCULATION",
      "\nFOR ADDITION +\nFOR SUBTRACTION -\nFOR MULIPLCATION *\nFOR DIVISION /\nFOR POWER **\nFOR PERCENTAGE % "
      "\nFor Modulus Reminder $")
# This function adds two numbers
def add(x,y):
    return x+y
# This function subtracts two numbers
def sub(x,y):
    return  x-y
# This function multiplies two numbers
def multi(x,y):
    return x*y
# This function divides two numbers
def div(x,y):
    return  x/y
# This function helps to find power. i.e; 2^3=8
def pow(m,l):
    return  m**l
# This Function used to Find Percentage.
def per(a,b):
    return a/b*100
# This Function is Used to Find Reminder of divide.
def mod_reminder(x,y):
    return x%y
while(True):
    cal = input("Enter your Calculation = ")
    if cal in ("+","-","*","/","$"):
        num1 = float(input("Enter your First Number = "))
        num2 = float(input("Enter your Second Number = "))
        if cal=="+":
            print("Your Answer is = ",add(num1,num2))
        elif cal=="-":
            print("Your Answer is = ", sub(num1,num2))
        elif cal=="*":
            print("Your Answer is = ", multi(num1,num2))
        elif cal=="/":
            print("Your Answer is = ", div(num1,num2))
        elif cal==("$"):
            print("Your Answer is = ", mod_reminder(num1,num2))
    if cal in ("**"):
        b = float(input("Enter The Base Number = "))
        e = float(input("Enter Exponancial = "))
        if cal=="**":
            print("Your Anwer is = ",pow(b,e))
    if cal in ("%"):
        q = float(input("Enter the number for Percentage = "))
        w = float(input("Enter Total Number = "))
        if cal=="%":
            print("Your Answer is = " , per(q,w),"%")
    if cal not in ("+","-","*","/","$","%","**"):
        print("Invalid")
