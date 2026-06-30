"""
============================================================
NUMPY (NUMERICAL PYTHON) - COMPLETE MASTERCLASS
============================================================

- Used for working with arrays.
- In Python we have lists that serve the purpose of arrays, but they are slow to process.
- NumPy is an incredible library to perform mathematical and statistical operations 
  due to its fast and memory-efficient nature as it is optimized to work with 
  latest CPU architectures.
- NumPy aims to provide an array object that is up to 50x faster than traditional 
  Python lists. So processes can access and manipulate them very efficiently.

============================================================
TOPICS COVERED:
============================================================
1.  Creating NumPy Arrays (All Ways)
2.  0-Dimensional Arrays (Scalar)
3.  1-Dimensional Arrays (Vector)
4.  Array Attributes
5.  Data Types & Type Priority
6.  Converting Between List and Array
7.  Accessing Elements (Indexing, Slicing, Boolean)
8.  Modifying Arrays (Replace, Insert, Append, Delete)
9.  Copying Arrays
10. Sorting Arrays
11. Arithmetic Operations
12. Comparison Operations
13. Mathematical/Statistical Operations
14. Reshaping Arrays
15. Stacking & Concatenation
16. Where & Filtering
============================================================
"""


# ============================================================
# IMPORT NUMPY
# ============================================================
import numpy as np


# ============================================================
# 1. CREATING NUMPY ARRAYS (ALL WAYS)
# ============================================================

# --- Method 1: From a Python List ---
l = [1, 2, 3, 4, 5]
arr = np.array(l)
print("From list:", arr)
# Output: From list: [1 2 3 4 5]

# --- Method 2: np.arange(start, stop, step) ---
arr2 = np.arange(0, 10, 2)
print("np.arange:", arr2)
# Output: np.arange: [0 2 4 6 8]

# --- Method 3: np.zeros(shape) ---
arr3 = np.zeros(5)
print("np.zeros:", arr3)
# Output: np.zeros: [0. 0. 0. 0. 0.]

# --- Method 4: np.ones(shape) ---
arr4 = np.ones(4)
print("np.ones:", arr4)
# Output: np.ones: [1. 1. 1. 1.]

# --- Method 5: np.full(shape, fill_value) ---
arr5 = np.full(5, 7)
print("np.full:", arr5)
# Output: np.full: [7 7 7 7 7]

# --- Method 6: np.linspace(start, stop, num) ---
arr6 = np.linspace(0, 10, 5)
print("np.linspace:", arr6)
# Output: np.linspace: [ 0.   2.5  5.   7.5 10. ]

# --- Method 7: np.random.randint(low, high, size) ---
arr7 = np.random.randint(1, 100, 5)
print("np.random.randint:", arr7)
# Output: np.random.randint: [45 12 78 33 91]  (Random each time)

# --- Method 8: np.random.rand(size) ---
arr8 = np.random.rand(5)
print("np.random.rand:", arr8)
# Output: np.random.rand: [0.234 0.567 0.891 0.123 0.456]  (Random each time)


# ============================================================
# 2. 0-DIMENSIONAL ARRAYS (SCALAR)
# ============================================================
# A single value. Created by passing a single number to np.array().
# int, float, bool, string → when converted into array → becomes 0D array

print("\n--- 0D Arrays ---")

# Integer
a1 = np.array(42)
print("0D int:", a1, "| ndim:", a1.ndim, "| shape:", a1.shape)
# Output: 0D int: 42 | ndim: 0 | shape: ()

# Float
a2 = np.array(3.14)
print("0D float:", a2, "| ndim:", a2.ndim, "| shape:", a2.shape)
# Output: 0D float: 3.14 | ndim: 0 | shape: ()

# Boolean
a3 = np.array(True)
print("0D bool:", a3, "| ndim:", a3.ndim, "| shape:", a3.shape)
# Output: 0D bool: True | ndim: 0 | shape: ()

# String
a4 = np.array("Hello")
print("0D string:", a4, "| ndim:", a4.ndim, "| shape:", a4.shape)
# Output: 0D string: Hello | ndim: 0 | shape: ()




