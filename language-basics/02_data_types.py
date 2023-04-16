"""
Built-in data types
-------------------
Text type     : str
Numeric types : int, float, complex
Sequence types: list, tuple, range
Mapping type  : dict
Set types     : set, frozenset
Boolean type  : bool
Binary types  : bytes, bytearray, memoryview
None type     : NoneType
"""

# ++++++++++ Getting the data type ++++++++++
print(type('53'))
print(type(5))
print(type(12.75))

# ++++++++++ Setting value & data type ++++++++++
x = "Hello World"
print(type(x)) # <class 'str'>

x = 20
print(type(x)) # <class 'int'>

x = 99.5
print(type(x)) # <class 'float'>

x = 1j
print(type(x)) # <class 'complex'>

x = ["mango", "kiwi", "cherry"]
print(type(x)) # <class 'list'>

x = ("apple", "banana", "strawberry")
print(type(x)) # <class 'tuple'>

x = range(6)
print(type(x)) # <class 'range'>

x = {"name" : "John", "age" : 36}
print(type(x)) # <class 'dict'>

x = {"apple", "banana", "cherry"}
print(type(x)) # <class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # <class 'frozenset'>

x = True
print(type(x)) # <class 'bool'>

x = b"Hello"
print(type(x)) # <class 'bytes'>

x = bytearray(5)
print(type(x)) # <class 'bytearray'>

x = memoryview(bytes(5))
print(type(x)) # <class 'memoryview'>

x = None
print(type(x)) # <class 'NoneType'>


# ++++++++++ Setting specific data type ++++++++++
x = str('Hello World!') # str
x = int(20) # int
x = float(20.5) # float
x = complex(1j) # complex
x = list(("apple", "banana", "cherry")) # list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict(name="John", age=36) # dict
x = set(("apple", "banana", "cherry")) # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(4) # bool
x = bytes(5) # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

