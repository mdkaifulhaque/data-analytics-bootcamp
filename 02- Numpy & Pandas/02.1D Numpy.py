import numpy as np

# ============================================================
# 3. 1-DIMENSIONAL ARRAYS (VECTOR)
# ============================================================
# A single row of values. Created by passing a list, tuple, or set.
# list, tuple, set, dict → when converted into array → becomes 1D array

print("\n--- 1D Arrays ---")

# From list
b1 = np.array([1, 2, 3, 4, 5])
print("1D from list:", b1, "| ndim:", b1.ndim, "| shape:", b1.shape)
# Output: 1D from list: [1 2 3 4 5] | ndim: 1 | shape: (5,)

# From tuple
b2 = np.array((10, 20, 30))
print("1D from tuple:", b2, "| ndim:", b2.ndim, "| shape:", b2.shape)
# Output: 1D from tuple: [10 20 30] | ndim: 1 | shape: (3,)

# From set (order may vary)
b3 = np.array({100, 200, 300})
print("1D from set:", b3, "| ndim:", b3.ndim, "| shape:", b3.shape)
# Output: 1D from set: [100 200 300] | ndim: 1 | shape: (3,)  (order may vary)

# Using ndmin to force dimension
b4 = np.array([1, 2, 3], ndmin=1)
print("1D with ndmin:", b4, "| ndim:", b4.ndim, "| shape:", b4.shape)
# Output: 1D with ndmin: [1 2 3] | ndim: 1 | shape: (3,)


# ============================================================
# 4. ARRAY ATTRIBUTES
# ============================================================

print("\n--- Array Attributes ---")
arr = np.array([1, 2, 3, 4, 5, 6])

print("ndim (dimensions):", arr.ndim)
# Output: ndim (dimensions): 1

print("shape (size per dimension):", arr.shape)
# Output: shape (size per dimension): (6,)

print("size (total elements):", arr.size)
# Output: size (total elements): 6

print("dtype (data type):", arr.dtype)
# Output: dtype (data type): int64

print("itemsize (bytes per element):", arr.itemsize)
# Output: itemsize (bytes per element): 8

print("nbytes (total bytes):", arr.nbytes)
# Output: nbytes (total bytes): 48


# ============================================================
# 5. DATA TYPES & TYPE PRIORITY
# ============================================================
# If any value is float and other is int → all convert to float
# Priority (Highest to Lowest):
#   1. string
#   2. float
#   3. int
#   4. bool

print("\n--- Data Types & Priority ---")

# All integers → int64
c1 = np.array([1, 2, 3])
print("All int:", c1.dtype)
# Output: All int: int64

# Mix of int and float → ALL become float64
c2 = np.array([1, 2.5, 3])
print("Int + Float:", c2.dtype)
# Output: Int + Float: float64

# Mix of int, float, and string → ALL become string
c3 = np.array([1, 2.5, "hello"])
print("Int + Float + String:", c3.dtype)
# Output: Int + Float + String: <U32

# Explicitly setting data type
c4 = np.array([1, 2, 3], dtype=float)
print("Explicit float:", c4, "| dtype:", c4.dtype)
# Output: Explicit float: [1. 2. 3.] | dtype: float64

# Type casting with astype()
c5 = np.array([1.5, 2.7, 3.9])
c5_int = c5.astype(int)
print("Type cast to int:", c5_int)
# Output: Type cast to int: [1 2 3]


# ============================================================
# 6. CONVERTING BETWEEN LIST AND ARRAY
# ============================================================

print("\n--- List ↔ Array Conversion ---")

# List → Array
my_list = [1, 2, 3, 4, 5]
arr_from_list = np.array(my_list)
print("List to array:", arr_from_list)
# Output: List to array: [1 2 3 4 5]

# Array → List
back_to_list = arr_from_list.tolist()
print("Array to list:", back_to_list, "| type:", type(back_to_list))
# Output: Array to list: [1, 2, 3, 4, 5] | type: <class 'list'>


# ============================================================
# 7. ACCESSING ELEMENTS
# ============================================================

print("\n--- Accessing Elements ---")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# --- 7a. Single Element via Indexing ---
print("\n[Single Element]")
print("Positive indexing arr[0]:", arr[0])    # First element
# Output: Positive indexing arr[0]: 10

print("Positive indexing arr[4]:", arr[4])    # Fifth element
# Output: Positive indexing arr[4]: 50

print("Negative indexing arr[-1]:", arr[-1])  # Last element
# Output: Negative indexing arr[-1]: 100

print("Negative indexing arr[-2]:", arr[-2])  # Second to last
# Output: Negative indexing arr[-2]: 90

# --- 7b. Multiple Elements via Slicing ---
print("\n[Slicing]")
print("arr[2:7]:", arr[2:7])       # Index 2 to 6
# Output: arr[2:7]: [30 40 50 60 70]

print("arr[:5]:", arr[:5])         # Start to index 4
# Output: arr[:5]: [10 20 30 40 50]

print("arr[5:]:", arr[5:])         # Index 5 to end
# Output: arr[5:]: [60 70 80 90 100]

print("arr[::2]:", arr[::2])       # Every 2nd element
# Output: arr[::2]: [10 30 50 70 90]

print("arr[::-1]:", arr[::-1])     # Reverse
# Output: arr[::-1]: [100  90  80  70  60  50  40  30  20  10]

print("arr[-4:-1]:", arr[-4:-1])   # Negative slicing
# Output: arr[-4:-1]: [70 80 90]

# --- 7c. Multiple Elements via Fancy Indexing ---
print("\n[Fancy Indexing]")
indices = [0, 2, 4, 6]
print("arr[[0,2,4,6]]:", arr[indices])
# Output: arr[[0,2,4,6]]: [10 30 50 70]

# --- 7d. Multiple Elements via Boolean/Conditional Indexing ---
print("\n[Boolean/Conditional Indexing]")
print("arr > 50:", arr[arr > 50])
# Output: arr > 50: [60 70 80 90 100]

print("Even numbers:", arr[arr % 20 == 0])
# Output: Even numbers: [20 40 60 80 100]

print("Between 30 and 80:", arr[(arr > 30) & (arr < 80)])
# Output: Between 30 and 80: [40 50 60 70]


# ============================================================
# 8. MODIFYING ARRAYS
# ============================================================

print("\n--- Modifying Arrays ---")

# --- 8a. Replace / Update ---
arr = np.array([1, 2, 3, 4, 5])
arr[0] = 100
print("After arr[0]=100:", arr)
# Output: After arr[0]=100: [100   2   3   4   5]

arr[1:3] = [200, 300]
print("After slice update:", arr)
# Output: After slice update: [100 200 300   4   5]

arr[arr > 100] = 0
print("After conditional update:", arr)
# Output: After conditional update: [  0 200 300   4   5]

# --- 8b. Insert ---
arr = np.array([1, 2, 3, 4, 5])
new_arr = np.insert(arr, 2, 99)
print("After insert at index 2:", new_arr)
# Output: After insert at index 2: [ 1  2 99  3  4  5]

# --- 8c. Append ---
arr = np.array([1, 2, 3])
new_arr = np.append(arr, [4, 5])
print("After append:", new_arr)
# Output: After append: [1 2 3 4 5]

# --- 8d. Delete ---
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, 2)
print("After delete index 2:", new_arr)
# Output: After delete index 2: [10 20 40 50]

new_arr2 = np.delete(arr, [0, 3])
print("After delete indices 0 and 3:", new_arr2)
# Output: After delete indices 0 and 3: [20 30 50]


# ============================================================
# 9. COPYING ARRAYS
# ============================================================

print("\n--- Copying Arrays ---")

# Assignment (=) → Alias (Shared Memory)
a = np.array([1, 2, 3])
b = a
b[0] = 999
print("After alias change, a:", a)  # Original changed!
# Output: After alias change, a: [999   2   3]

# View (Shallow Copy)
a = np.array([1, 2, 3])
b = a.view()
b[0] = 888
print("After view change, a:", a)   # Original STILL changed!
# Output: After view change, a: [888   2   3]

# Deep Copy (Independent)
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 777
print("After copy change, a:", a)   # Original is SAFE!
# Output: After copy change, a: [1 2 3]

print("After copy change, b:", b)
# Output: After copy change, b: [777   2   3]


# ============================================================
# 10. SORTING ARRAYS
# ============================================================

print("\n--- Sorting Arrays ---")
arr = np.array([5, 2, 8, 1, 9, 3])

sorted_arr = np.sort(arr)
print("Sorted:", sorted_arr)
# Output: Sorted: [1 2 3 5 8 9]

print("Original (unchanged):", arr)
# Output: Original (unchanged): [5 2 8 1 9 3]

# Sorting strings
names = np.array(["Charlie", "Alice", "Bob"])
print("Sorted names:", np.sort(names))
# Output: Sorted names: ['Alice' 'Bob' 'Charlie']


# ============================================================
# 11. ARITHMETIC OPERATIONS
# ============================================================

print("\n--- Arithmetic Operations ---")
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("a + b:", a + b)
# Output: a + b: [11 22 33 44]

print("a - b:", a - b)
# Output: a - b: [-9 -18 -27 -36]

print("a * b:", a * b)
# Output: a * b: [ 10  40  90 160]

print("b / a:", b / a)
# Output: b / a: [10. 10. 10. 10.]

print("b % a:", b % a)
# Output: b % a: [0 0 0 0]

print("a ** 2:", a ** 2)
# Output: a ** 2: [ 1  4  9 16]

# Scalar operations
print("a * 10:", a * 10)
# Output: a * 10: [10 20 30 40]

print("a + 5:", a + 5)
# Output: a + 5: [6 7 8 9]


# ============================================================
# 12. COMPARISON OPERATIONS
# ============================================================

print("\n--- Comparison Operations ---")
a = np.array([1, 5, 10, 15, 20])

print("a > 10:", a > 10)
# Output: a > 10: [False False False  True  True]

print("a == 10:", a == 10)
# Output: a == 10: [False False  True False False]

print("a <= 5:", a <= 5)
# Output: a <= 5: [ True  True False False False]

print("a != 10:", a != 10)
# Output: a != 10: [ True  True False  True  True]


# ============================================================
# 13. MATHEMATICAL / STATISTICAL OPERATIONS
# ============================================================

print("\n--- Mathematical Operations ---")
arr = np.array([10, 20, 30, 40, 50])

print("sum:", np.sum(arr))
# Output: sum: 150

print("mean:", np.mean(arr))
# Output: mean: 30.0

print("median:", np.median(arr))
# Output: median: 30.0

print("min:", np.min(arr))
# Output: min: 10

print("max:", np.max(arr))
# Output: max: 50

print("std:", np.std(arr))
# Output: std: 14.142135623730951

print("var:", np.var(arr))
# Output: var: 200.0

print("argmin (index of min):", np.argmin(arr))
# Output: argmin (index of min): 0

print("argmax (index of max):", np.argmax(arr))
# Output: argmax (index of max): 4

print("cumsum:", np.cumsum(arr))
# Output: cumsum: [ 10  30  60 100 150]

print("cumprod:", np.cumprod(arr))
# Output: cumprod: [     10     200    6000  240000 12000000]


# ============================================================
# 14. RESHAPING ARRAYS (1D only)
# ============================================================

print("\n--- Reshaping (1D) ---")
arr = np.arange(1, 13)
print("Original:", arr)
# Output: Original: [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Reshape to 1D with different size (must have same total elements)
reshaped = arr.reshape(12, 1)
print("Reshaped to (12,1):", reshaped)
# Output: Reshaped to (12,1):
# [[ 1]
#  [ 2]
#  [ 3]
#  [ 4]
#  [ 5]
#  [ 6]
#  [ 7]
#  [ 8]
#  [ 9]
#  [10]
#  [11]
#  [12]]

# Flatten (if it were 2D, but keeping 1D context)
print("Flatten:", arr.flatten())
# Output: Flatten: [ 1  2  3  4  5  6  7  8  9 10 11 12]


# ============================================================
# 15. STACKING & CONCATENATION (1D only)
# ============================================================

print("\n--- Stacking & Concatenation ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("hstack:", np.hstack((a, b)))
# Output: hstack: [1 2 3 4 5 6]

print("concatenate:", np.concatenate((a, b)))
# Output: concatenate: [1 2 3 4 5 6]


# ============================================================
# 16. WHERE & FILTERING
# ============================================================

print("\n--- Where & Filtering ---")
arr = np.array([1, 5, 8, 12, 15, 20])

# Replace values based on condition
result = np.where(arr > 10, "Big", "Small")
print("np.where result:", result)
# Output: np.where result: ['Small' 'Small' 'Small' 'Big' 'Big' 'Big']

# Get indices where condition is True
indices = np.where(arr > 10)
print("Indices where > 10:", indices)
# Output: Indices where > 10: (array([3, 4, 5]),)


# ============================================================
print("\n" + "="*50)
print("✅ END OF NUMPY MASTERCLASS (0D & 1D ONLY)")
print("="*50)
