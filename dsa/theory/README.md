# <ins>Python Data Structures & Algorithms</ins>

## Important Links
[GeeksForGeeks](https://www.geeksforgeeks.org/python-data-structures-and-algorithms/)
[w3schools](https://www.w3schools.com/python/)

## Topics Covered

- [Lists](#lists)
- [Tuple](#tuple)
- [Set](#set)
- [Frozen Sets](#frozen-sets)
- String
- Dictionary
- Matrix
- Bytearray
- LinkedList
- LinkedList Traversal
- Stack
- Queue
- Priority Queue
- Heap
- Binary Tree
- Tree Traversal
- Binary Search Tree
- Graphs
- Graph Traversal
- Recursion
- Dynamic Programming
- Searching Algorithms
  - Binary Search
- Sorting Algorithms
  - Selection Sort
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Shell Sort

### Lists

- Ordered collection of data just like arrays in other languages
- Allows different data types
- Python List implementation is similar to Vectors in C++ or ArrayList in Java
- Operations like inserting or deleting element from the beginning of the list is expensive as elements are required to be shifted
- Insertion and deletion at the end of the list is mostly efficient, however it can be costly in the scenario where the pre-allocated memory is full

```python
list = [1, 2, 3, "ABC", 2.3]
print(list)
```

- List elements can be accessed by the assigned index
- Index start from 0, and ends at N-1 where N is the length/size of the list

![GFG - Python List image](https://media.geeksforgeeks.org/wp-content/uploads/List-Slicing.jpg)

```python
list1 = [1, 2, 3, "ABC", 2.3]
print(list1)

# Multi-dimensional list
list2 = [['apple', 'orange'], 'basket']
print(list2)

# Accessing elements
print(list1[0])
print(list1[2])

print(list2[0]) # ['apple', 'orange']
print(list2[0][1]) # orange
print(list2[1]) # basket

print(list2[-1]) # Last element i.e., basket
print(list1[-3]) # Third last element i.e., 3
```

### Tuple

- Tuples are similar to Lists, but Tuples are immutable in nature i.e., once created it cannot be modified
- Just like a List, a Tuple can also contain elements of various types
- Tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping of the data sequence

> Note: To create a tuple of one element there must be a trailing comma. For example: ```(8,)``` will create a tuple containing 8 as the element.

```python
mytuple = ('red', 'green', 'blue')
print(mytuple)

# Accessing element using indexing
print(mytuple[0]) # First element i.e., 'red'
print(mytuple[-1]) # Last element i.e., 'blue'
print(mytuple[-2]) # 2nd last element i.e., 'green'
```

### Set

- Python set is a mutable collection of data that does not allow any duplication
- Sets are basically used to include membership testing and eliminating duplicate entries
- Set is unindexed i.e., we cannot be sure in which order the items will appear, hence accessing via index is not possible
- To get the length of set use the ```len()``` function
- The data structure used in this is Hashing (a popular technique to perform insertion, deletion, and traversal in O(1) on average)
- If multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List
- In CPython Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity
- To add items to set use the ```add()``` method
- To add items from another set or other data structures, use the ```update()``` method
- Use the ```union()``` method to return a new set by combining all items from both sets
- To remove an item in a set, use the ```remove()```, or the ```discard()``` method.
- We can also use the ```pop()``` method to remove an item, but this method will remove a random item, so we cannot be sure what item that gets removed. The return value of the ```pop()``` method is the removed item.
- The ```clear()``` method empties the set
- The ```del``` keyword will delete the set completely
- The ```intersection_update()``` method will keep only the items that are present in both sets
- The ```intersection()``` method will return a new set, that only contains the items that are present in both sets
- The ```symmetric_difference_update()``` method will keep only the elements that are NOT present in both sets
- The ```symmetric_difference()``` method will return a new set, that contains only the elements that are NOT present in both sets
- [List of built-in set methods](https://www.w3schools.com/python/python_sets_methods.asp)

> Note: The values ```True``` and ```1``` are considered the same value in sets, and are treated as duplicates

Set implementation:

![GFG - Set implementation as HashTable](https://media.geeksforgeeks.org/wp-content/uploads/HashTable.png)

Sets with numerous operations on a single HashTable:

![GFG - Multiple entries on an index in set](https://media.geeksforgeeks.org/wp-content/uploads/Hasing-Python.png)

```python
myset = {'apple', 'cherry', 'orange'}
print(myset)

myset2 = set((1, 2, 'Geeks', 4, 'For', 6, 'Life')) # Using the set() Constructor
print(myset2)

# Accessing element using for loop
myset = {'apple', 'cherry', 'orange'}
for el in myset:
  print(el)

# Checking existance of an element
myset2 = set((1, 2, 'Geeks', 4, 'For', 6, 'Life'))
print('Geeks' in myset2)

# Add item to set
myset = {'apple', 'cherry', 'orange'}
myset.add('banana')

# Join two sets using union()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
myset = set1.union(set2) # {'b', 'c', 2, 3, 1, 'a'} 

# Add items from one set to another (update method)
myset = {'apple', 'cherry', 'orange'}
tropical = {'pineapple', 'mango', 'papaya'}
myset.update(tropical) # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

# Add items a non set to a set using the update() method
myset = {'apple', 'cherry', 'orange'}
tropical = ['pineapple', 'mango']
myset.update(tropical) # {'apple', 'mango', 'cherry', 'pineapple', 'banana'}

# Remove item using remove() method
# If the item to remove does not exist, remove() will raise an error.
myset = {'apple', 'cherry', 'orange'}
myset.remove('cherry')

# Remove item using discard() method
# If the item to remove does not exist, discard() will NOT raise an error.
myset = {'apple', 'cherry', 'orange'}
myset.discard('cherry')

# Remove a random item using pop() method
myset = {'apple', 'cherry', 'orange'}
popped_item = myset.pop()
print(popped_item)

# Clear the set using the clear() method
myset = {'apple', 'cherry', 'orange'}
myset.clear()

# Delete set
myset = {'apple', 'cherry', 'orange'}
del myset

# Keep ONLY the Duplicates [intersection_update(), intersection()]
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.intersection_update(y)
print(x) # {'apple'}

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)
print(z) # {'apple'}

# Keep all, but NOT the duplicates [symmetric_difference_update(), symmetric_difference()]
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y)
print(x) # {'google', 'banana', 'microsoft', 'cherry'}

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)
print(x) # {'google', 'banana', 'microsoft', 'cherry'}
```

### Frozen Sets

- These are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.
- While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

```python
frozen_set = frozenset(['e', 'f', 'g'])
print(frozen_set)
frozen_set.add('h') # This line would throw an error
```

