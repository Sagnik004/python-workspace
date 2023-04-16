# ++++++++++ Variable data Type gets inferred at runtime ++++++++++
x = 4
x = "Demo"
print(x)

# ++++++++++ Casting ++++++++++
x = str(3)
y = int('55')
z = float('23.50')
print(x, y, z)

# ++++++++++ Get type ++++++++++
x = 5
y = 'Hello'
z = 43.55
print(type(x), type(y), type(z))

# ++++++++++ Case sensitive ++++++++++
a = 54
A = '55'
print(a, A)
print(type(a), type(A))

"""
Naming Conventions
----------------------
- Can have short names, or more descriptive names
- Must start with a letter or the underscore character
- Cannot start with a number
- Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Case sensitive
- Cannot be any reserved keywords
"""
# ++++++++++ Legal names ++++++++++
myvar = 'John'
my_var = 'John'
_my_var = 'John'
myVar = 'John'
MYVAR = 'John'
myvar2 = 'John'

# ++++++++++ Illegal names ++++++++++
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# ++++++++++ Multiple variable assignments in a single statement ++++++++++
# But make sure the number of variables matches the number of values, 
# or else we will get an error.
x, y, z = 84, 'test', 11.25
print(x, y, z)
print(type(x), type(y), type(z))

# One value to multiple variables
x = y = z = 99
print(x, y, z)
print(type(x), type(y), type(z))

# ++++++++++ Unpacking a collection ++++++++++
# If we have a collection of values in a list, tuple etc. 
# Python allows us to extract the values into variables. This is called unpacking.
# But we need to unpack all of them, else we will get an error
fruits = ["apple", "kiwi", "orange"]
x, y, z = fruits
print(x, y, z)

# ++++++++++ Global Variables ++++++++++
# Variables which are created outside of the function
# Can be used all, both inside function and outside
x = 'awesome'

def myfn():
  print('Python is ' + x)

myfn()

# Variable with same name as global variable inside function will
# act as local variable to the function. Global variable will
# retain its value
x = 'awesome!'

def myfn():
  x = 'cool'
  print('Python is ' + x)

myfn()
print(x)

# ++++++++++ Global keyword ++++++++++
# generally variables created inside function are local, and have function scope.
# To create a global variable inside a function, we can use the "global" keyword.
def myfunc():
  global x
  x = 'created with global keyword'

myfunc()
print(x)

# To change a global variable from inside a function, "global"
# keyword can be used
x = 'awesome'

def myfunc():
  global x
  x = 'changed via global keyword'

myfunc()
print('I am ' + x)

