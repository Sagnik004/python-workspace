# ++++++++++ 3 numeric types in Python ++++++++++
# int, float, complex

x = 1   # int
y = 2.8 # float
z = 1j  # complex

print(type(x))
print(type(y))
print(type(z))

# ++++++++++ int ++++++++++
# whole number positive or negative, without decimals, unlimited length
x = 1
y = 356562225548877110908008987678767889976565
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# ++++++++++ float ++++++++++
# number positive or negative, contains 1 or more decimals
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# ++++++++++ complex ++++++++++
# written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# ++++++++++ Type conversion ++++++++++
# we can convert from one type to another with the int(), float(), and complex() methods
# we cannot convert complex numbers into another number type
x = 1   # int
y = 2.8 # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 

# ++++++++++ Random Number ++++++++++
# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers
import random
print(random.randrange(1, 10))

