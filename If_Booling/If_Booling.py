# Function input must get a string
x1 = int(input("Please input first number:"))
x2 = int(input("please input second number"))
if x1>200:
    print("x>200")
elif x1==200:
    print("x=200")
else:
    print("X<200")

op = input("Please operation: +,-,*,/")
if op == "+":
    print(x1+x2)
elif op == "-":
    print(x1-x2)
elif op == "*":
    print(x1*x2)
elif op == "/":
    print(x1/x2)
else:
    print("Wrong type")

