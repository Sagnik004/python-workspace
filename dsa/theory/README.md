# <ins>Python Data Structures & Algorithms</ins>

## Important Links
[GeeksForGeeks](https://www.geeksforgeeks.org/python-data-structures-and-algorithms/)

## Topics Covered

- [Lists](#lists)
- [Tuple](#tuple)
- Set
- Frozen Sets
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

