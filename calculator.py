num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
oper = input ("Enter the operator:")

if oper == "*":
    ans = num1 * num2
    print (num1,oper,num2,"=",ans)

elif oper == "/":
    ans = num1 / num2
    print (num1,oper,num2,"=",ans)

elif oper == "+":
    ans = num1 + num2
    print (num1,oper,num2,"=",ans)

elif oper == "-":
    ans = num1 - num2
    print (num1,oper,num2,"=",ans)