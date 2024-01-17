# a = "raw_input()"
# for i in a:
#   print (i)


# a = "user"
# count = 0
# for i in a:
#   count = count+1
# print (count)

# a = "umbrella"
# # if e in a:
# print('e' in 'umbrella')

# a = "this is orange juice"
# print('orange' in 'this is orange juice')


# a = 11
# b = 2
# print(a//b)

# a = 11.0
# b = 2
# print(a//b)

# a = -16
# b = 3
# print(a//b)

# i = 2
# print(i)
# i += 1
# print(i)

# x = 5
# y = 10
# print(5**2>25 and y<50)


# x= 5
# y =10
# z = 5**2
# print(z>25 and y<50)

# a = 2+3
# b = -2
# c =(6-8/2*4**2*2)
# z = a+b*c
# print(z)

# a = 4
# b = 8
# a,b = b,a
# print(a,b)

# a = 4
# b = 6
# temp = a
# a = b
# b = temp
# print(a,b)

## calculator
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)
 

# x = 10
# y = 20
# print(x+y)

### calculator
num1 = int(input("enter your number:"))
num2 = int(input("enter your number:"))
select = input("select (add,sub,mul,div,modu,floordivision):")
if select =="add" :
    result = num1+num2
    print(num1 "+" num2 "=" num1+num2)  
elif select == "sub": 
    result = num1 - num2
    print(f"num1 - num2 = {result}")
elif select == "mul":
    result = num1 * num2
    print(f"num1 * num2 = {result}")
elif select == "div":
    result = num1 / num2
    print(f"num1 / num2 = {result}")
elif select == "modu":
    result = num1 % num2
    print(f"num1 % num2 = {result}")
elif select == "floordivision":
    result = num1 // num2
    print(f"num1 // num2 = {result}")    
else:
    print("invalid number")    
