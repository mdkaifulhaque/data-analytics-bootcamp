'''
# 1. Tuple : A tuple is an ordered, immutable collection that can store multiple data types, allows duplicate values, and preserves insertion order.

# 2. Creating Tuples : Tuples can be created using parentheses (), comma-separated values, or the tuple() constructor, and a single-element tuple requires a trailing comma.

# 3. Accessing Elements : Use positive indexing, negative indexing, and slicing to retrieve one or more elements without modifying the original tuple.

# 4. Packing & Unpacking : Packing groups multiple values into one tuple, while unpacking assigns tuple elements directly to multiple variables.

# 5. Immutability : Tuples cannot be modified after creation, but if they contain mutable objects like lists, those objects can still be changed.

# 6. Operations : Tuples support concatenation (+), repetition (*), membership (in/not in), iteration, comparison, and most sequence operations.

# 7. Built-in Functions & Methods : Functions like len(), min(), max(), sum(), sorted(), any(), and all() work with tuples, while tuples provide only count() and index() methods.

# 8. Copying & Memory : Assigning a tuple creates another reference (alias), and since tuples are immutable, separate copying is rarely needed except for nested mutable objects.

# 9. Tuple vs List : Tuples are immutable, faster, and memory-efficient, whereas lists are mutable, flexible, and suitable for frequently changing data.
'''

# 1. Creation & The "Syntax Trap"
# 1. Standard Creation
t1 = (1, 2, 3, "srk", True, 3.14)
print(t1)  # Output: (1, 2, 3, 'srk', True, 3.14)

# 2. Tuple Packing (Parentheses are optional!)
t2 = 10, 20, 30
print(type(t2))  # Output: <class 'tuple'>

# 3. Empty Tuple
empty = ()
print(type(empty))  # Output: <class 'tuple'>

# 4. THE SINGLE ELEMENT TRAP (Classic Interview Question)
t3 = (10)
print(type(t3))  # Output: <class 'int'> -> Python thinks it's just math parentheses!

# ✅ The Fix: Add a trailing comma
t4 = (10,)
print(type(t4))  # Output: <class 'tuple'> -> Now it's a tuple!



# 2. Accessing Elements: Indexing
tup = ("kaif", 23, 43, 23.4, True, [50, 40], (99, 23, 12))

# 1. Positive Indexing (Starts at 0)
print(tup[0])   # Output: kaif
print(tup[2])   # Output: 43

# 2. Negative Indexing (Starts at -1 from the end)
print(tup[-1])  # Output: (99, 23, 12)
print(tup[-2])  # Output: [50, 40]

# 3. Nested Indexing (Drilling down into nested structures)
# Goal: Get the number 99 from the nested tuple at the very end
print(tup[-1][0])       # Output: 99

# Goal: Get the number 40 from the nested list
print(tup[-2][1])       # Output: 40



 # 3. Slicing Tuples
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,[10, 11, 12], (13, 14, 15))

print(nums[2:7])    # Output: (2, 3, 4, 5, 6)
print(nums[:5])     # Output: (0, 1, 2, 3, 4)
print(nums[5:])     # Output: (5, 6, 7, 8, 9)
print(nums[::2])    # Output: (0, 2, 4, 6, 8)
print(nums[::-1])   # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0) -> Reverses!
print(nums[-1][1])  # Output: 14 -> Accessing nested tuple
print(nums[-2][2])  # Output: 12 -> Accessing nested list

# Corner Cases (Just like lists, slicing never throws an IndexError)
print(nums[100:])   # Output: () -> Empty tuple
print(nums[5:2])    # Output: () -> Empty tuple


# 4. Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# 1. Concatenation (+)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 6)

# 2. Repetition (*)
t4 = t1 * 3
print(t4)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 3. Membership Operators (in / not in)
print(2 in t1)      # Output: True
print(10 not in t1) # Output: True


# 5. The Immutability Rule & The "Gotcha" (Crucial for Interviews 
# The Rule: You cannot reassign, add, or remove elements from a tuple

T = (4, 3, 2, 1)
# T[1] = 20  # ❌ TypeError: 'tuple' object does not support item assignment


# The "Gotcha": Mutable Elements Inside an Immutable Tuple
# What if a tuple contains a mutable object, like a list? The tuple cannot change which list it points to, but the list itself can be modified!
t3 = (1, 2, 3, 4, 5, [6, 7, 8])

# ❌ CANNOT change the reference to the list
# t3[5] = [60, 70, 80]  # TypeError!

# ✅ CAN change the internal contents of the list
t3[5][0] = 60  
print(t3)  # Output: (1, 2, 3, 4, 5, [60, 7, 8]) -> The list inside changed!



# 6. Iterating & Looping
colors = ("red", "green", "blue")

# 1. Standard For-Loop
for color in colors:
    print(color)

# 2. Using enumerate() to get index and value
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")



# 8. Tuple Methods & Built-in Functions
# Because you cannot modify a tuple, Python provides only two built-in methods.
t = (10, 20, 30, 20, 40, 20)

# 1. count(value): Returns the number of times a value appears
print(t.count(20))  # Output: 3

# 2. index(value): Returns the index of the first occurrence
print(t.index(30))  # Output: 2
# print(t.index(100)) # ❌ ValueError: 100 is not in tuple


# You can use all the standard Python math and size functions on tuples.
nums = (5, 2, 8, 1, 9)

print(len(nums))    # 5 (Number of elements)
print(min(nums))    # 1 (Smallest element)
print(max(nums))    # 9 (Largest element)
print(sum(nums))    # 25 (Sum of elements)

# ⚠️ Note on sorted():
# sorted() returns a LIST, not a tuple!
sorted_nums = sorted(nums)
print(type(sorted_nums))  # Output: <class 'list'>


# 9. Tuple Unpacking (A Massive Python Feature)
# 1. Basic Unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30

# 2. Swapping Variables (No temporary variable needed!)
a, b = 1, 2
a, b = b, a  # Python creates a tuple (b, a) and unpacks it into (a, b)
print(a, b)  # Output: 2 1

# 3. The Asterisk (*) Operator (Python 3+)
# Use * to grab the "rest" of the elements as a list
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]  <- Notice it becomes a list!
print(last)    # Output: 5


# 10. Modifying a Tuple 
# Since tuples are immutable, you cannot change them directly. However, you can convert them to a list, modify the list, and convert it back to a tuple.
tuples = (12, 32, 45)

# Step 1: Convert to a List
l = list(tuples)

# Step 2: Modify the List
l[1] = 99
l.append(100)

# Step 3: Convert back to a Tuple
tuples = tuple(l)

print(tuples)  # Output: (12, 99, 45, 100)



#  11. Deleting Tuples
t = (1, 2, 3, 4)
del t

# print(t)  # ❌ NameError: name 't' is not defined



# 12. Tuples vs Lists
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 1. Memory Efficiency
# Lists over-allocate memory to make appends faster. Tuples allocate exact memory.
print(sys.getsizeof(my_list))   # Output: 120 bytes 
print(sys.getsizeof(my_tuple))  # Output: 80 bytes  

# 2. Speed
# Tuples are faster to iterate over because they are stored in a continuous 
# block of memory and their size is fixed.

# 3. Hashability (Crucial for Dictionaries)
# Because tuples are immutable, they can be used as Dictionary keys.
my_dict = { (1, 2): "Coordinates" }  # ✅ Works!
# my_dict = { [1, 2]: "Coordinates" } # ❌ TypeError: unhashable type: 'list'


