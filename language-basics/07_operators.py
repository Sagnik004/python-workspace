'''
Python divides the operators in the following groups:
  - Arithmetic operators
  - Assignment operators
  - Comparison operators
  - Logical operators
  - Identity operators
  - Membership operators
  - Bitwise operators
'''

# Arithmetic operators
'''
  +  -> Addition
  -  -> Subtraction
  *  -> Multiplication
  /  -> Division
  %  -> Modulus
  ** -> Exponentiation
  // -> Floor division
'''
print(5+2)
print(5-2)
print(5*3)
print(5/2) # 2.5 will be the answer, to get only int part cast it
print(5%2)
print(5**3) # 5^3 = 5*5*5 = 125
print(22//7) # rounds the result down to the nearest whole number

# Assignment operators
'''
  =   -> x = 5
  +=  -> x = x + 3
  -=  -> x = x - 3
  *=  -> x = x * 3
  /=  -> x = x / 3
  %=  -> x = x % 3
  //= -> x = x // 3
  **= -> x = x ** 3
  &=  -> x = x & 3
  |=  -> x = x | 3
  ^=  -> x = x ^ 3
  >>= -> x = x >> 3
  <<= -> x = x << 3
'''

# Comparison operators
'''
  == -> Equal; x == y
  != -> Not equal; x != y
  >  -> Greater than; x > y
  <  -> Less than; x < y
  >= -> Greater than or equal to; x >= y
  <= -> Less than or equal to; x <= y
'''

# Logical operators
'''
  and -> Returns True if both statements are true
  or  -> Returns True if one of the statements is true
  not -> Reverse the result, returns False if the result is true [not(x < 5 and x < 10)]
'''

print('------------------------')
# Identity operators
#   Used to compare the objects, not if they are equal in values, but if they are actually 
#   the same object, with the same memory location.
'''
  is -> Returns True if both variables are the same object
  is not -> Returns True if both variables are not the same object
'''
x = ['apple', 'banana']
y = ['apple', 'banana']
z = x
print(x is z)
print(x is y)
print(x == y) # Value comparison
print(x is not z)
print(x is not y)
print(x != y) # Value comparison

print('------------------------')
# Membership operators
# used to test if a sequence is presented in an object.
'''
  in -> Returns True if a sequence with the specified value is present in the object
  not in -> Returns True if a sequence with the specified value is not present in the object
'''
x = ['apple', 'banana']
print('banana' in x)
print('pineapple' in x)
print('pineapple' not in x)

# Bitwise operators
'''
  &  -> AND; Sets each bit to 1 if both bits are 1
  |  -> OR;  Sets each bit to 1 if one of two bits is 1
  ^  -> XOR; Sets each bit to 1 if only one of two bits is 1
  ~  -> NOT; Inverts all the bits
  << -> Zero fill left shift; Shift left by pushing zeros in from the right and let the leftmost bits fall off
  >> -> Signed right shift; Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
'''

# Operator Precedence
# Precedence order below, highest to lowest
'''
()  Parentheses
**  Exponentiation
+x -x ~x -> Unary plus, unary minus, and bitwise NOT
* / // % -> Multiplication, division, floor division, and modulus
+ - -> Addition and subtraction
<< >> -> Bitwise left and right shifts
& -> Bitwise AND
^ -> Bitwise XOR
| -> Bitwise OR
==  !=  >  >=  <  <=  is  is not  in  not in -> Comparisons, identity, and membership operators
not -> Logical NOT
and -> AND
or -> OR
'''
# If two operators have the same precedence, the expression is evaluated from left to right.



