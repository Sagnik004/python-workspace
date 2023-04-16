# One of two values: True or False
# We can evaluate any expression in Python to get bool value.

print(10 > 9)
print(10 == 9)
print(10 < 9)

print('------------------------')
a = 200
b = 33
if b > a:
  print('b > a')
else:
  print('a > b')

print('------------------------')
# The bool() function allows us to evaluate any value, and return True or False
print(bool('Hello'))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print('------------------------')
# Most Values are True
'''
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
print(bool('abc'))
print(bool(123))
print(bool(['apple', 'cherry', 'banana']))

print('------------------------')
# Some values are False
'''
There are not many values that evaluate to False, except empty values 
such as (), [], {}, '', the number 0, and the value None. And of course 
the value False evaluates to False.
'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that 
# is if we have an object that is made from a class with a __len__ function 
# that returns 0 or False.
print('------------------------')
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print('------------------------')
# Functions can return a Boolean
def myfunc():
  return True

if (myfunc()):
  print('YES!')
else:
  print('NOO!')

print('------------------------')
# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to determine if an
# object is of a certain data type
x = 200
print(isinstance(x, int))




