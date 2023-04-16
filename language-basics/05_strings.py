# ++++++++++ Multiline Strings ++++++++++
# we can use 3 double quotes or single quotes
# in the result, the line breaks are inserted at the same position as in the code
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# ++++++++++ Strings are arrays ++++++++++
# Like many other languages strings in Python are arrays of bytes representing 
# unicode characters. Python does not have a character data type, a single 
# character is simply a string with a length of 1. Square brackets [] can be used 
# to access elements of the string (0 indexed).
a = "Hello, World!"
print(a[1])

# ++++++++++ Looping through strings ++++++++++
for x in 'banana':
  print(x)

# ++++++++++ String Length ++++++++++
# use len() function
a = "Hello, World!"
print(len(a))

# ++++++++++ Check String ++++++++++
# check if a certain phrase or character is present in a string.
# we can use the keyword "in"
txt = 'The best things in life are free!'
print('free' in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, 
# we can use the keyword "not in"
txt = 'The best things in life are free!'
print('expensive' not in txt)

txt = 'The best things in life are free!'
if 'expensive' not in txt:
  print('No, \'expensive\' is NOT present.')


# ++++++++++ Slicing Strings ++++++++++
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5]) # llo

# Slice from start
b = "Hello, World!"
print(b[:5]) # Hello

# Slice till the end
b = "Hello, World!"
print(b[2:]) # llo, World!

# Negative Indexing (get from end)
b = "Hello, World!"
print(b[-2]) # d
print(b[-6:]) # World!
print(b[-5:-2]) # orl


# ++++++++++ Modify Strings ++++++++++
# upper() -> returns the string in upper case
a = 'Hello World!'
print(a.upper()) # HELLO WORLD!

# lower() -> returns the string in lower case
a = 'Bugs BuNNy'
print(a.lower()) # bugs bunny

# strip() -> removes any whitespace from the beginning or the end
a = ' Hello, World! '
print(a.strip()) # Hello, World!

# replace() -> replaces a string with another string
a = 'Hello, World!'
print(a.replace("H", "J")) # Jello, World!

# split() -> splits the string into substrings if it finds instances of the separator
a = 'Hello, World!'
print(a.split(", ")) # ['Hello', 'World!'] 


# ++++++++++ String Concatenation ++++++++++
# Using the plus (+) operator
a = 'Hello'
b = 'World'
c = a + ' ' + b
print(c)


# ++++++++++ Format Strings ++++++++++
# we cannot combine strings and numbers using the plus operator
# print('My name is Drogo and my age is ' + 54)
# (err = TypeError: can only concatenate str (not "int") to str)

# but we can combine using "format()" method
age = 36
txt = 'My name is John, and my age is {}'
print(txt.format(age))

# "format()" can take unlimited count of arguments
item_qty = 3
item_number = 567
item_price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(item_qty, item_number, item_price))

# we can use index numbers to be sure the arguments 
# are placed in the correct placeholders
item_qty = 3
item_number = 567
item_price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(item_qty, item_number, item_price))

# ++++++++++ Escape Characters ++++++++++
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is 
# surrounded by double quotes. To fix it we can use the escape character.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

"""
Escape Characters
-----------------
\' -> single quote
\\ -> backslash
\n -> new line
\r -> carriage return
\t -> tab
\b -> backspace
\f -> form feed
"""
# \ooo -> octal value
# \xhh -> hex value


# ++++++++++ String Methods ++++++++++
# All below string methods return new string, as strings are immutable
# in Python as well

# capitalize() -> Converts the first character to upper case, and remaining all lower
txt = 'python is FUN!'
x = txt.capitalize()
print(x)

txt = "36 is my age."
x = txt.capitalize()
print(x)

# casefold() -> Converts and returns a string where all the characters are lower case
#               lower() is a similar method, but casefold() covers much more characters
txt = 'Hello, And Welcome To My World!'
x = txt.casefold()
print(x) 

# center() -> center align the string, using a specified character
#             (space is default) as the fill character
txt = 'banana'
x = txt.center(20)
print(x)

txt = ' apple '
x = txt.center(20, '+')
print(x)

# count() -> returns the number of times a specified value appears in the string
# syntax: string.count(value, start, end); start and end are optional, defaults to 
# 0 and end of string
txt = 'I love apples, apple are my favorite fruit'
x = txt.count('apple')
print(x) # 2

txt = 'I love apples, apple are my favorite fruit'
x = txt.count('apple', 10, 24)
print(x) # 1

# encode() -> encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
# Syntax: string.encode(encoding=encoding, errors=errors)
# errors = specifying the error method. Legal values are -
#    'backslashreplace' -> uses a backslash when encoding of a character errors out
#    'ignore' -> ignores the characters that cannot be encoded
#    'namereplace' -> replaces the character with a text explaining the character
#    'strict' -> Default, raises an error on failure
#    'replace' -> replaces the character with a questionmark
#    'xmlcharrefreplace' -> replaces the character with an xml character
txt = "My name is Ståle"
print(txt.encode())
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

# endswith() -> returns True if the string ends with the specified value, otherwise False
# Syntax: string.endswith(value, start, end) 
# start & end are optional
txt = 'Hello, welcome to my world.'
x = txt.endswith('.')
print(x)
print(txt.endswith('my world.'))
print(txt.endswith('my world.', 5, 11))

# expandtabs() -> sets the tab size to the specified number of whitespaces. Default is 8
# syntax: string.expandtabs(tabsize)
txt = 'H\te\tl\tl\to'
print(txt.expandtabs()) # H       e       l       l       o
print(txt.expandtabs(2)) # H e l l o
print(txt.expandtabs(10)) # H         e         l         l         o

# find() -> finds the first occurrence of the specified value.
# Syntax: string.find(value, start, end)   start, end are optional
# Returns -1 if the value is not found.
# Almost same as index() method, only difference is that the index() method 
# raises an exception if the value is not found.
txt = 'Hello, welcome to my world.'
print(txt.find('welcome'))
print(txt.find('e'))
print(txt.find('e', 5, 10))
print(txt.find('q')) # -1 i.e., not found
# print(txt.index('q'))  -- raises exception

# format() -> formats the specified value(s) and insert them inside the string's placeholder.
# defined using curly brackets: {}
# returns the formatted string
# Syntax: string.format(value1, value2...)
# Placeholders can be identified using named indexes {price}, numbered indexes {0}, 
# or even empty placeholders {}
txt = 'For only {price:.2f} dollars!'
print(txt.format(price = 49))
txt1 = 'My name is {fname}, I\'m {age} years old.'.format(fname = "John", age = 36)
txt2 = 'My name is {0}, I\'m {1}.'.format("John",36)
txt3 = 'My name is {}, I\'m {}.'.format("John",36)
print(txt1, txt2, txt3)

# Formatting Types
# :< Left aligns the result (within the available space)
print('We have {:<8} chickens.'.format(49))
# :> Right aligns the result (within the available space)
print('We have {:>8} chickens.'.format(99))
# :^ Center aligns the result (within the available space)
print('We have {:^8} chickens.'.format(31))
# := Places the sign to the left most position
print('The temperature is {:=8} degrees celsius.'.format(-5))
# :+ Use a plus sign to indicate if the result is positive or negative
print('The temperature is between {:+} and {:+} degrees celsius.'.format(-3, 7))
# :- Use a minus sign for negative values only
print('The temperature is between {:-} and {:-} degrees celsius.'.format(-3, 7))
# : Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
print('The temperature is between {: } and {: } degrees celsius.'.format(-3, 7))
# :, Use a comma as a thousand separator
print('The universe is {:,} years old.'.format(13800000000))
# :_ Use a underscore as a thousand separator
print('The universe is {:_} years old.'.format(13800000000))
# :b binary format
print('The binary version of {0} is {0:b}'.format(5))
# :c Converts the value into the corresponding unicode character
# :d Decimal format
print('We have {:d} chickens.'.format(0b101))
# :e Scientific format, with a lower case e
print('We have {:e} chickens.'.format(5))
# :E Scientific format, with an upper case E
print('We have {:E} chickens.'.format(5))
# :f Fix point number format
print('The price is {:.2f} dollars.'.format(45))
print('The price is {:f} dollars.'.format(44))
# :F Fix point number format, in uppercase format (show inf and nan as INF and NAN)
x = float('inf')
print('The price is {:F} dollars.'.format(x))
print('The price is {:f} dollars.'.format(x))
# :g General format
# :G General format (using a upper case E for scientific notations)
# :o Octal format
print('The octal version of {0} is {0:o}'.format(10))
# :x Hex format, lower case
print('The Hexadecimal version of {0} is {0:x}'.format(255))
# :X Hex format, upper case
print('The Hexadecimal version of {0} is {0:X}'.format(255))
# :n Number format
# :% Percentage format
print('You scored {:%}'.format(0.25))
print('You scored {:.0%}'.format(0.25))

# index() -> finds the first occurrence of the specified value.
# Raises an exception if the value is not found.
# Same as find(), just that find() returns -1 if value not found.
# Syntax: string.index(value, start, end)
print('Hello, welcome to my world.'.index('e'))
print('Hello, welcome to my world.'.index('e', 5, 10))
# print('Hello, welcome to my world.'.index('q')) -- throws exception

# isalnum() -> returns True if all the characters are alphanumeric, 
# meaning alphabet letters (a-z) and numbers (0-9). Example of characters that are 
# not alphanumeric: (space)!#%&? etc.
print('Company12'.isalnum()) # True
print('Company 12'.isalnum()) # False

# isalpha() -> 

# isdecimal() ->

# isdigit() ->

# isidentifier() ->

# islower() ->

# isnumeric() ->

# isprintable() ->

# isspace() ->

# istitle() ->

# isupper() ->

# join() ->

# ljust() ->

# lower() ->

# lstrip() ->

# maketrans() ->

# partition() ->

# replace() ->

# rfind() ->

# rindex() ->

# rjust() ->

# rpartition() ->

# rsplit() ->

# rstrip() ->

# split() ->

# splitlines() ->

# startswith() ->

# strip() ->

# swapcase() ->

# title() ->

# translate() ->

# upper() ->

# zfill() ->








