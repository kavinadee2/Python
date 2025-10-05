#calculator
n1=float(input("Enter a First Number: "))
opr=input("Choose a operator(+ - * / % **): ")
n2=float(input("Enter a Second Number: "))

if(opr=="+"):
    result=n1+n2
elif(opr=="-"):
    result=n1-n2
elif(opr=="*"):
    result=n1*n2
elif(opr=="/"):
    result=n1/n2
elif(opr=="%"):
    result=n1%n2
elif(opr=="**"):
    result=n1**n2
else:
    print(f"you enter operator is not a operator😥")
print(f"{n1} {opr} {n2} = {result}")

