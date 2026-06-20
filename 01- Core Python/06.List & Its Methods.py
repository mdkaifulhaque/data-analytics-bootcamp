
'''
 - it is one of the most used datatype in python and is very flexible
 - List is Advance Data type, where it can store multiple values
 - Each value inside the list is called an items
 - A list can have from 0 items to multiple items
 - Declaring a list is, items separated by commas are enclosed within brackets []
 - All the items in a list do not need to be of the same type (heterogenous)
 - List is an ordered sequence of items.
 - items can be duplicated (list items can be repeated)
 - List is Mutable. the items can be modified with in the same object
 # Empty List : List with o items
'''

'''
## VALUES - WE HAVE THREE KIND OF VALUES 
   1. NUMERICAL - Int, Float, Complex
   2. BOOLEAN -  True , False
   3. NON-NUMERICAL - String, List, Tuple, Dictionaries 

   --- COMPLEX VALUES MEANS --- 
   There are called real values and imaginary values both values of the combination that's called complex value
   What i mean by for EX: " values = 2.4 + 3j  " so left side is real value and right side is imaginary value
   if i want to extract real value then we used use Values.real or if i want to extract imaginary value we use to use values.imag

'''

# 1. Creating Lists 
empty_list = []
numbers = [10, 20, 30]
mixed = ["Rakesh", 20, 85.5, True]  # Python lists are heterogeneous

print(mixed) 
# Output: ['Rakesh', 20, 85.5, True]




# 2. Nested Lists (Lists inside lists)
# Think of this like a matrix or a table
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]



# 3. Accessing List Elements
fruits = ["apple", "banana", "mango", "grapes"]

print(fruits[0])   # Output: apple (First element)
print(fruits[-1])  # Output: grapes (Last element)

# ⚠️ Corner Case: Index out of range
# print(fruits[10])  # IndexError: list index out of range



# 4. List Slicing
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:7])    # Output: [2, 3, 4, 5, 6] (Index 2 to 6)
print(nums[:5])     # Output: [0, 1, 2, 3, 4] (Start from beginning)
print(nums[5:])     # Output: [5, 6, 7, 8, 9] (Go to the end)
print(nums[::2])    # Output: [0, 2, 4, 6, 8] (Step of 2)
print(nums[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (Reverse list!)

# ⚠️ Corner Case: Slicing never throws an IndexError!
print(nums[100:])   # Output: [] (Returns empty list, doesn't crash)
print(nums[5:2])    # Output: [] (If start > stop with positive step, returns empty)




# 5. Mutability & Operations
# Unlike Strings (which are immutable), Lists are mutable. You can change them in place.

# 1. Updating Elements
lst = [10, 20, 30]
lst[1] = 99
print(lst)  # Output: [10, 99, 30]

# 2. Concatenation (+) and Repetition (*)
a = [1, 2]
b = [3, 4]
print(a + b)    # Output: [1, 2, 3, 4]
print(a * 3)    # Output: [1, 2, 1, 2, 1, 2]

# 3. Membership Operators (Checking if an item exists)
print(10 in lst)     # Output: True
print(100 not in lst) # Output: True



# 6. Essential List Methods

# ➕ Adding Elements
l = [1, 2, 3]

# append(): Adds exactly ONE item to the end.
l.append(4)          # l is now [1, 2, 3, 4]
l.append([5, 6])     # l is now [1, 2, 3, 4, [5, 6]] -> Adds the list as a single object!

# extend(): Adds multiple items from an iterable to the end.
l = [1, 2, 3]
l.extend([4, 5])     # l is now [1, 2, 3, 4, 5] -> Unpacks the list!
l.extend("AB")       # l is now [1, 2, 3, 4, 5, 'A', 'B'] -> Strings are iterables too!

# insert(): Adds an item at a specific index. insert(index, element)
l = ['a', 'c', 'd']
l.insert(1, 'b')     # l is now ['a', 'b', 'c', 'd']


# ➖ Removing Elements
l = [10, 20, 30, 20, 40]

# remove(): Removes the FIRST occurrence of a VALUE.
l.remove(20)         # l is now [10, 30, 20, 40]
# l.remove(100)      # ⚠️ ValueError: 100 not in list

# pop(): Removes and RETURNS an item by INDEX. Defaults to the last item.
removed = l.pop()    # removed is 40, l is now [10, 30, 20]
removed = l.pop(1)   # removed is 30, l is now [10, 20]
# [].pop()           # ⚠️ IndexError: pop from empty list

# del: A keyword, not a method. Can delete by index or slice.
l = [1, 2, 3, 4, 5]
del l[0]             # l is now [2, 3, 4, 5]
del l[1:3]           # l is now [2, 5]



# 7. Sorting & Reversing
nums = [3, 1, 4, 1, 5]

# sort(): Sorts the list IN-PLACE (modifies original). Returns None.
nums.sort()                  # nums is now [1, 1, 3, 4, 5]
nums.sort(reverse=True)      # nums is now [5, 4, 3, 1, 1]

# sorted(): Returns a NEW sorted list. Original remains unchanged.
original = [3, 1, 2]
new_list = sorted(original)  # new_list is [1, 2, 3], original is still [3, 1, 2]

# reverse(): Reverses the list IN-PLACE.
nums = [1, 2, 3]
nums.reverse()               # nums is now [3, 2, 1]



# 8. The Danger Zone: Copying & Aliasing 

# This is where most beginners make mistakes. Understanding memory references is crucial.
# ❌ The Aliasing Problem (Using =)

a = [1, 2, 3]
b = a        # 'b' is just a new name (alias) for the exact same list in memory!

b[0] = 999
print(a)     # Output: [999, 2, 3] -> 'a' changed too!



# ✅ Shallow Copy (Using .copy() or [:])

a = [1, 2, 3]
b = a.copy()  # Creates a new list in memory with the same values
# OR
c = a[:]      # Slicing the whole list also creates a shallow copy

b[0] = 999
print(a)      # Output: [1, 2, 3] -> 'a' is safe!
print(b)      # Output: [999, 2, 3]


# ❌ The Shallow Copy Trap (Nested Lists)
# If your list contains other lists (nested), .copy() only copies the outer list. The inner lists are still shared references!
# Solution: Use deepcopy from the copy module for nested structures.

matrix = [[1, 2], [3, 4]]
copy_matrix = matrix.copy()

copy_matrix[0][0] = 99
print(matrix)       # Output: [[99, 2], [3, 4]] -> The inner list changed!

# ✅ Deep Copy (Using copy.deepcopy())
import copy
deep_copy = copy.deepcopy(matrix) # Now they are 100% independent.


# 9. List Comprehensions
# List comprehensions provide a concise way to create lists. The basic syntax is:
# [expression for item in iterable if condition] 

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]






