# Lists are used to store multiple items in a single variable.
### List is a collection which is ordered and changeable. Allows duplicate members.
# list = ["apple","banana","cherry"]
# print(list)

# ##length 
# list = ["apple","banana","cherry"]
# print(len(list))

##type
# list = ["apple","banana","cherry"]
# print(type(list))

# ##list() 
# mylist = list(("apple","banana","cherry"))
# print(mylist)

# ##datatypes
# list = ["apple","True",99]
# print(list)

##acess list
# list = ["apple","banana","cherry"]
# print(list[1])

# ##neagtive indexing 
# list = ["apple","banana","cherry"]
# print(list[-1])

## Range of indexing
# list = ["apple","banana","cherry","mango","melon"]
# print(list[2:4])


# list = ["apple","banana","cherry","mango","melon"]
# print(list[:4])


# list = ["apple","banana","cherry","mango","melon"]
# print(list[2:])


# list = ["apple","banana","cherry","mango","melon"]
# print(list[-4:-1])

# # check if them in list
# list = ["apple","banana","cherry","mango","melon"]
# if "apple" in list:
#     print("yes, 'apple' in the fruits list")

#to check fruitsin list or not
# a = input("enter the fruit name:")
# list = ["apple","banana","cherry","mango","melon"]
# if a.lower() in list:
#     print(f"Yes, '{a}' is in the list.")
# elif a.lower() not in list:
#     print(f"No, '{a}' is not in the list.")


##change the item value
# list = ["appple","banana","cherry"]
# list[1] = "mango"
# print(list)

##change a range of item list
# list = ["apple","banana","cherry","mango","melon"]
# list[1:3] = ["blackcurrent","orange"]
# print(list)

# list = ["apple", "banana", "cherry"]
# list[1:2] = ["blackcurrant", "watermelon"]
# print(list)

## insert method
# list = ["appple","banana","cherry"]
# list.insert(2,"melon")
# print(list)

##append
# list = ["appple","banana","cherry"]
# list.append("mango")
# print(list)

## Extend list
# list = ["appple","banana","cherry"]
# mylist = ["app","bus","car"]
# list.extend(mylist)
# print(list)

## add any iterable like tuple
# list = ["appple","banana","cherry"]
# mylist = ("app","bus")
# list.extend(mylist)
# print(list)

# ##remove
# list = ["appple","banana","cherry"]
# list.remove("banana")
# print(list)

# #pop
# list = ["appple","banana","cherry"]
# list.pop(1)
# print(list)


# list = ["appple","banana","cherry"]
# list.pop()
# print(list)

# #del
# list = ["appple","banana","cherry"]
# del list[1]
# print(list)

#del list
# list = ["appple","banana","cherry"]
# del list
# print(list)

# ##clear
# list = ["appple","banana","cherry"]
# list.clear()
# print(list)

# ##loops
# list = ["appple", "banana", "cherry"]
# for x in list:
#     print(x)


# loop through the index 
# list = ["appple", "banana", "cherry"]
# for x in range(len(list)):
#     print(x)

# list = ["appple", "banana", "cherry"]
# for x in range(len(list)):
#     print(list[x])

## while loop
# list = ["apple","banana","cherry"]
# i = 0
# while i < len(list):
#     print(list[i])
#     i = i+1

## list comphersion
# list = ["appple", "banana", "cherry"]
# new_list = []
# for x in list:
#     if "a" in x:
#         new_list.append(x)
# print(list)

# list = ["appple", "banana", "cherry"]
# new_list = [x for x in list if "a" in x]
# print(new_list)


# ## comdition 
# list = ["apple","banana","cherry","mango","melon"]
# new_list = [x for x in list if x != "apple"]
# print(new_list)

## without if 
# list = ["apple","banana","cherry","mango","melon"]
# new_list = [x for x in list]
# print(new_list)

# ## iterable 
# list = [x for x in range(10)]
# print(list)

#with condition
# list = [x for x in range(10) if x < 6]
# print(list)

# ## expresiion
# list = ["apple","banana","cherry","mango","melon"]
# new = [x.upper()  for x in list]
# print(new)

# list = ["apple","banana","cherry","mango","melon"]
# new = ['hi' for x in list ]
# print(new)

# list = ["apple","banana","cherry","mango","melon"]
# new = [x if x != "banana" else "orange" for x in list]
# print(new)


## sort lists
# list = ["apple","orange","banana","cherry","mango","melon"]
# list.sort()
# print(list)

#sort num
# num = [2,6,1,4,9,0]
# num.sort()
# print(num)

## sort descending
# list = ["apple","banana","cherry","mango","melon"]
# list.sort(reverse=True)
# print(list)

# using num
# num =[4,7,0,1]
# num.sort(reverse=True)
# print(num)


## customized sort function
# def myfun(n):
#     return abs(n -50)
# list = [100,50,65,88,23]
# list.sort(key = myfun)
# print(list)

## case insenstive sort to captial first then lower 
# list = ["apple","Banana","cherry","Mango","melon"]
# list.sort()
# print(list)

# lowwer
# list = ["apple","Banana","cherry","mango","melon"]
# list.sort(key =str.lower)
# print(list)

##reverse
# list = ["apple","banana","cherry","mango","melon"]
# list.reverse()
# print(list)

#3 copy a list
# list = ["apple","banana","cherry","mango","melon"]
# mylist = list.copy()
# print(list)

# list1 = ["apple","banana","cherry","mango","melon"]
# mylist = list(list1)
# print(mylist)

##join lists
# list1 = ["a","b","c"]
# list2 = [1,2,3]
# list3 =list1+list2
# print(list3)

#append
# list1 = ["a","b","c"]
# list2 = [1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1)    

# ##extend
# list1 = ["a","b","c"]
# list2 = [1,2,3]
# list1.extend(list2)
# print(list1)
