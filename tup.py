#A tuple is a collection which is ordered and unchangeable.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# tuple = ("apple","banana","cherry")
# print(tuple)

#tuple allows duplicates
# tuple = ("apple","banana","cherry","apple")
# print(tuple)

#length
# tuple = ("apple","banana","cherry")
# print(len(tuple))

# creating single tuple
# tuple = ("apple",)
# print(tuple)

#tuple aloows datatypes
# tuple = ("apple","banana","cherry")
# tuple1 =(1,2,3)
# tuple2=(True)
# print(tuple)
# print(tuple1)
# print(tuple2)

# # tuple type
# tuple = ("apple","banana","cherry")
# print(type(tuple))


#tuple constructor
# tuple1 =tuple(("apple","banana","cherry"))
# print(tuple1)

## acess tuple
# tuple = ("apple","banana","cherry")
# print(tuple[1])

# # negative 
# tuple = ("apple","banana","cherry")
# print(tuple[-1])

# tuple = ("apple","banana","cherry","mango","melon","orange")
# print(tuple[2:5])

#not print melon
# tuple = ("apple","banana","cherry","mango","melon","orange")
# print(tuple[:4])

#print from cherry
# tuple = ("apple","banana","cherry","mango","melon","orange")
# print(tuple[2:])


# check if item exists
tuple = ("apple", "banana", "cherry")
if "apple" in tuple:
  print("Yes, 'apple' is in the fruits tuple")