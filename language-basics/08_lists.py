# Lists store multiple items in a single variable
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#   *Set items are unchangeable, but we can remove and/or add items whenever we like.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#   **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Create a list
alist = ['apple', 'banana', 'cherry']
print(alist)

# ----- List items -----
# List items are ordered, changeable, and allow duplicate values
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered: items have a defined order, and that order will not change. If we add new items 
#          to a list, the new items will be placed at the end of the list. There are some
#          list methods that will change the order, however in general they are ordered.
# Changeable: we can change, add, and remove items in a list after it has been created.
# Allow Duplicates: Since lists are indexed, lists can have items with the same value
blist = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(blist)

# List Length: use the len() function to determine how many items a list have.
clist = ['apple', 'banana', 'cherry']
print(len(clist))

# List items can be of any data type
list1 = ['apple', 'banana', 'cherry']
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ['abc', 34, True, 40, 'male']
print(list1, list2, list3, list4)

# Data type of List
# lists are defined as objects with the data type 'list'
dlist = ['apple', 'banana', 'cherry']
print(type(dlist)) # <class 'list'>

# The list() constructor
# It is also possible to use the list() constructor when creating a new list.
elist = list(('apple', 'banana', 'cherry')) # note the double round-brackets
print(elist)

# --------- Access List Items ---------



