
#This is a comment
# This is comment. -- Single line comment

"""
Project description:
This is a python lesson
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
from curses.ascii import isupper
from http.cookiejar import uppercase_escaped_char

fname  = "Prathmesh" #Str
age = 27
height = 5.6

print("Data type of Fname is " , type(fname))
print("Data type of age is " , type(age))
print("Data type of height is " , type(height))

#List
grocery = ["Bread","Milk", "Chocolates","Rice"]
Fruits = ["Mango","Apples","watermelon","Orange"]
Mobiles = ["Apple","Samsung","Nokia","Realme","Xiomi","Lava","Motorola"]
Mobiles[0]
print(Mobiles[1])

#Tuples
Fruits = ("Mango","Apples","watermelon","Orange")


cart = ["Apple iphone 16","Apple Earpods","Plastic storage"]
print("there are ",len(cart),"Items in the cart")

lname = "sangam"
print(isupper(lname))
