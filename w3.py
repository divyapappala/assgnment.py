# Q1
#print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

#Q2
# import sys
# print("python version")
# print(sys.version)
# print("version info")
# print(sys.version_info)

#Q3
# from datetime import datetime
# current_datetime = datetime.now()
# print(current_datetime)

#Q5
# firstname = input("enter your firstname:")
# lastname = input("enter your lastname:")
# reverse_name = lastname+ " " +firstname
# print("reversed_names:",reverse_name)

#Q6
# digit = input("enter the numbers seperated by commas:")
# number_list = digit.split(",")
# number_tuple = tuple(number_list)
# print(number_list)
# print(number_tuple)

# #Q7
# file = input("enter your filename:")
# f_extns = file.split(".")
# print("the extension of file is :" + repr(f_extns[-1]))

# #Q8
# list=["red","green","blue","yellow"]
# print(list[0],list[-1])

#Q9
# exam_st_date =(11,12,2014)
# print("the examination will start from:, %i/%i/%i" % exam_st_date)

#Q10
# n = int(input("enter the number:"))
# temp = str(n)
# temp1=temp+temp
# temp2=temp+temp+temp
# cal = n +int(temp1) + int(temp2)
# print(cal) 

#Q12
# import calendar
# y = int(input("enter the year:"))
# m = int(input("enter the month:"))
# print(calendar.month(y,m))

# #Q14
# from datetime import datetime
# date1 = datetime.strptime("11/2/2023", "%d/%m/%y")
# date2 = datetime.strptime("22/2/2023", "%d/%m/%y")
# # difference = relativedelta.relativedelta(date2, date1)
# difference = relativedelta.relativedelta(date2, date1)
# print(difference.months, "months", difference.days, "days")

# #type convertion
# x = 1
# y = 2.4
# z = 1j
# a = float(x)
# b = int(y)
# c = complex(z)
# print(a)
# print(b)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))
##



# ##random number
# import random
# print(random.randrange(1,10))


#len()
# a = "hello,world !"
# print(len(a))

# #for 
# for x in "bananna":
#     print(x)

# # replace string
# a = "hello,world"
# print(a.replace("h","J"))

# #split
# a = "hello,world"
# print(a.split(","))

# #string concatenation
# a = "hello"
# b ="world"
# c = a+b
# print(c)

#adding space between two 
# a ="hello"
# b = "world"
# c = a+ " " +b
# print(c)

#format
# age = 36
# txt = "my anme is john Iam {}"
# print(txt.format(age))

# qulaity  = 22
# item = 4
# price  = 456
# txt = "i want {} pieces and i have {} items and {} dollars" 
# print(txt.format(qulaity,item,price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price)) 

# Booleans 
# print(10 > 9)
# print(10==9)
# print(10 < 9)

# # using if statement 
# a = 200
# b = 22
# if b >a :
#     print(" b is greater than a ")
# else:
#     print(" b is not greater than a ")

# # evelate using string in bool
# print(bool("hello"))
# print(bool(15))

## operators 
### arithematic operators
# a = 4
# b = 5
# print(a+b)


# #subtraction
# a = 3
# b = 4
# print(a-b)

# #multiplivcation
# a = 4
# b = 2
# print(a * b)

# #division
# a = 5
# b = 8
# print(a/b)

# #modulus
# a = 5
# b  =  6
# print(a%b)
# # exponentition
# a  = 5
# b =8
# print(a**b)
# #floor division
# a = 14
# b = 2
# print(a//b)

# ### assignment operators
# a = 2
# print(a)
# + =
# a = 3
# a = a+2
# print(a)

# #-=
# a = 3
# a = a-1
# print(a)

a = 5
a^=3 
print(a)