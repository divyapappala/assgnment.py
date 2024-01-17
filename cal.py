a  = int(input("enter the number:"))
b = int(input("enter the number:"))
select = input("select operation(add,sub,mul,div,modu,explo,floordiv:)")
if select == "add":
    #value = a+b
    print(f"{a} + {b} = {a+b}")
elif select == "sub":
    #value = a-b
    print(f"{a} - {b} = {a-b}")
elif select  == "mul":
    print(f"{a}  * {b} = {a*b} ")   
elif select == "div":
    print(f"{a}  / {b} = {a/b}")
elif select == "modu":
    print(f"{a} % {b} = {a%b}")
elif select == "explo":
    print(f"{a} ** {b} = {a**b}")
elif select == "floordiv":
    print(f"{a} // {b} = {a//b}")
else:
    print("invalid syntax") 