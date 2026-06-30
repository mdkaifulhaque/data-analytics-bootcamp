"""
============================================================
NUMPY 2D ARRAYS 
============================================================

- 2D arrays (matrices) are the foundation of linear algebra, image processing,
  and data science in Python.
- A 2D array is an array of arrays — each row is itself a 1D array.
- NumPy provides powerful tools for creating, manipulating, and computing on matrices.

============================================================
TOPICS COVERED:
============================================================
1.  Creating 2D NumPy Arrays
2.  np.nan in Arrays
3.  zeros, ones, full with 2D shapes
4.  Special Matrices (eye, diag, zeros, ones)
5.  Array Attributes (ndim, shape, size, dtype)
6.  Indexing & Slicing (single value, row, column, sub-matrix)
7.  Data Modification (replace values, rows, columns)
8.  Arithmetic & Comparison Operations
9.  Mathematical Operations (with axis parameter)
10. Reshaping, Transpose, Flatten
11. Stacking (hstack, vstack)
============================================================
"""


# ============================================================
# IMPORT NUMPY
# ============================================================
import numpy as np


# ============================================================
# 1. CREATING 2D NUMPY ARRAYS
# ============================================================

# --- From Nested Lists ---
x = np.array([[1, 2, 3],
              [4, 5, 6]])
print("2D array x:")
print(x)
# Output:
# [[1 2 3]
#  [4 5 6]]

y = np.array([[7,  8,  9],
              [10, 11, 12],
              [13, 14, 15]])
print("\n2D array y:")
print(y)
# Output:
# [[ 7  8  9]
#  [10 11 12]
#  [13 14 15]]


# ============================================================
# 2. np.nan IN ARRAYS
# ============================================================
# np.nan represents "Not a Number" (missing/undefined values)
# When nan is present, the array becomes float type

print("\n--- np.nan in Arrays ---")
a = np.array([1, 2, 3, 4, 5, np.nan])
print("Array with nan:", a)
print("Data type:", a.dtype)
# Output:
# Array with nan: [ 1.  2.  3.  4.  5. nan]
# Data type: float64


# ============================================================
# 3. zeros, ones, full WITH 2D SHAPES
# ============================================================

print("\n--- zeros, ones, full (2D) ---")

# zeros: 3 rows, 4 columns
z1 = np.zeros((3, 4))
print("np.zeros((3,4)):")
print(z1)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# zeros with integer dtype
z2 = np.zeros((3, 4), dtype=int)
print("\nnp.zeros((3,4), dtype=int):")
print(z2)
# Output:
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

# ones: 2 rows, 3 columns
o1 = np.ones((2, 3))
print("\nnp.ones((2,3)):")
print(o1)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]

# ones with integer dtype
o2 = np.ones((2, 3), dtype=int)
print("\nnp.ones((2,3), dtype=int):")
print(o2)
# Output:
# [[1 1 1]
#  [1 1 1]]

# full: 2 rows, 4 columns, filled with 7
f1 = np.full((2, 4), 7)
print("\nnp.full((2,4), 7):")
print(f1)
# Output:
# [[7 7 7 7]
#  [7 7 7 7]]


# ============================================================
# 4. SPECIAL MATRICES (eye, diag, zeros, ones)
# ============================================================

print("\n--- Special Matrices ---")

# --- Identity Matrix (eye) ---
e1 = np.eye(3)
print("np.eye(3) - 3x3 Identity Matrix:")
print(e1)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Non-square identity (4 rows, 3 columns)
e2 = np.eye(4, 3)
print("\nnp.eye(4, 3) - 4x3 Identity Matrix:")
print(e2)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# --- Diagonal Matrix (diag) ---
d1 = np.diag([1, 2, 3])
print("\nnp.diag([1, 2, 3]) - Main Diagonal:")
print(d1)
# Output:
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

# Diagonal shifted RIGHT by 1 (k=1)
d2 = np.diag([1, 2, 3], k=1)
print("\nnp.diag([1, 2, 3], k=1) - Diagonal shifted right by 1:")
print(d2)
# Output:
# [[0 1 0 0]
#  [0 0 2 0]
#  [0 0 0 3]
#  [0 0 0 0]]

# Diagonal shifted LEFT by 1 (k=-1)
d3 = np.diag([1, 2, 3], k=-1)
print("\nnp.diag([1, 2, 3], k=-1) - Diagonal shifted left by 1:")
print(d3)
# Output:
# [[0 0 0 0]
#  [1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]]

# Diagonal shifted RIGHT by 2 (k=2)
d4 = np.diag([1, 2, 3], k=2)
print("\nnp.diag([1, 2, 3], k=2) - Diagonal shifted right by 2:")
print(d4)
# Output:
# [[0 0 1 0 0]
#  [0 0 0 2 0]
#  [0 0 0 0 3]
#  [0 0 0 0 0]
#  [0 0 0 0 0]]

# --- Zero Matrix (all zeros) ---
zm = np.zeros((3, 3), dtype=int)
print("\nZero Matrix 3x3:")
print(zm)
# Output:
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

# --- Ones Matrix (all ones) ---
om = np.ones((2, 4), dtype=int)
print("\nOnes Matrix 2x4:")
print(om)
# Output:
# [[1 1 1 1]
#  [1 1 1 1]]


# ============================================================
# 5. ARRAY ATTRIBUTES (2D)
# ============================================================

print("\n--- Array Attributes ---")
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("ndim (dimensions):", arr.ndim)
# Output: ndim (dimensions): 2

print("shape (rows, cols):", arr.shape)
# Output: shape (rows, cols): (3, 4)

print("size (total elements):", arr.size)
# Output: size (total elements): 12

print("dtype:", arr.dtype)
# Output: dtype: int64

print("itemsize (bytes per element):", arr.itemsize)
# Output: itemsize (bytes per element): 8

print("nbytes (total bytes):", arr.nbytes)
# Output: nbytes (total bytes): 96


# ============================================================
# 6. INDEXING & SLICING IN 2D ARRAY
# ============================================================

print("\n--- Indexing & Slicing ---")
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]])

# --- 6a. Single Value ---
print("\n[Single Value]")
print("matrix[0, 0] (row 0, col 0):", matrix[0, 0])
# Output: matrix[0, 0] (row 0, col 0): 10

print("matrix[1, 2] (row 1, col 2):", matrix[1, 2])
# Output: matrix[1, 2] (row 1, col 2): 70

print("matrix[-1, -1] (last row, last col):", matrix[-1, -1])
# Output: matrix[-1, -1] (last row, last col): 120

# --- 6b. Single Row ---
print("\n[Single Row]")
print("matrix[0] (first row):", matrix[0])
# Output: matrix[0] (first row): [10 20 30 40]

print("matrix[-1] (last row):", matrix[-1])
# Output: matrix[-1] (last row): [ 90 100 110 120]

# --- 6c. Multiple Rows ---
print("\n[Multiple Rows]")
print("matrix[0:2] (rows 0 and 1):")
print(matrix[0:2])
# Output:
# [[10 20 30 40]
#  [50 60 70 80]]

print("\nmatrix[1:] (row 1 to end):")
print(matrix[1:])
# Output:
# [[ 50  60  70  80]
#  [ 90 100 110 120]]

# --- 6d. Single Column ---
print("\n[Single Column]")
print("matrix[:, 0] (first column):", matrix[:, 0])
# Output: matrix[:, 0] (first column): [10 50 90]

print("matrix[:, -1] (last column):", matrix[:, -1])
# Output: matrix[:, -1] (last column): [ 40  80 120]

# --- 6e. Multiple Columns ---
print("\n[Multiple Columns]")
print("matrix[:, 1:3] (columns 1 and 2):")
print(matrix[:, 1:3])
# Output:
# [[ 20  30]
#  [ 60  70]
#  [100 110]]

# --- 6f. Sub-Matrix (rows AND columns) ---
print("\n[Sub-Matrix]")
print("matrix[0:2, 1:3] (rows 0-1, cols 1-2):")
print(matrix[0:2, 1:3])
# Output:
# [[20 30]
#  [60 70]]

# --- 6g. Boolean/Conditional Indexing ---
print("\n[Boolean Indexing]")
print("Elements > 50:")
print(matrix[matrix > 50])
# Output: Elements > 50: [ 60  70  80  90 100 110 120]

print("\nEven elements:")
print(matrix[matrix % 20 == 0])
# Output: Even elements: [ 20  40  60  80 100 120]


# ============================================================
# 7. DATA MODIFICATION OF 2D ARRAY
# ============================================================

print("\n--- Data Modification ---")

# --- 7a. Replace a Single Value ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix[1, 1] = 99
print("After matrix[1,1] = 99:")
print(matrix)
# Output:
# [[ 1  2  3]
#  [ 4 99  6]
#  [ 7  8  9]]

# --- 7b. Replace Multiple Values (via slicing) ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix[0:2, 1:3] = 0
print("\nAfter matrix[0:2, 1:3] = 0:")
print(matrix)
# Output:
# [[1 0 0]
#  [4 0 0]
#  [7 8 9]]

# --- 7c. Replace a Single Row ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix[1] = [100, 200, 300]
print("\nAfter replacing row 1:")
print(matrix)
# Output:
# [[  1   2   3]
#  [100 200 300]
#  [  7   8   9]]

# --- 7d. Replace a Single Column ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix[:, 1] = [20, 50, 80]
print("\nAfter replacing column 1:")
print(matrix)
# Output:
# [[ 1 20  3]
#  [ 4 50  6]
#  [ 7 80  9]]

# --- 7e. Replace Multiple Rows ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
matrix[0:2] = [[100, 200, 300],
               [400, 500, 600]]
print("\nAfter replacing rows 0 and 1:")
print(matrix)
# Output:
# [[100 200 300]
#  [400 500 600]
#  [  7   8   9]
#  [ 10  11  12]]

# --- 7f. Replace Multiple Columns ---
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
matrix[:, 1:3] = [[20, 30],
                  [60, 70],
                  [100, 110]]
print("\nAfter replacing columns 1 and 2:")
print(matrix)
# Output:
# [[  1  20  30   4]
#  [  5  60  70   8]
#  [  9 100 110  12]]

# --- 7g. Replace via Condition ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix[matrix > 5] = 0
print("\nAfter matrix[matrix > 5] = 0:")
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 0]
#  [0 0 0]]


# ============================================================
# 8. ARITHMETIC & COMPARISON OPERATIONS
# ============================================================

print("\n--- Arithmetic Operations ---")
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[10, 20],
              [30, 40]])

print("a + b:")
print(a + b)
# Output:
# [[11 22]
#  [33 44]]

print("\na * b (element-wise):")
print(a * b)
# Output:
# [[ 10  40]
#  [ 90 160]]

print("\na ** 2:")
print(a ** 2)
# Output:
# [[ 1  4]
#  [ 9 16]]

print("\nScalar: a * 10:")
print(a * 10)
# Output:
# [[10 20]
#  [30 40]]

print("\n--- Comparison Operations ---")
print("a > 2:")
print(a > 2)
# Output:
# [[False False]
#  [ True  True]]

print("\na == b:")
print(a == b)
# Output:
# [[False False]
#  [False False]]


# ============================================================
# 9. MATHEMATICAL OPERATIONS (with axis parameter)
# ============================================================

print("\n--- Mathematical Operations ---")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Sum of ALL elements:", np.sum(matrix))
# Output: Sum of ALL elements: 45

print("\nSum along axis=0 (column-wise sum):", np.sum(matrix, axis=0))
# Output: Sum along axis=0 (column-wise sum): [12 15 18]

print("\nSum along axis=1 (row-wise sum):", np.sum(matrix, axis=1))
# Output: Sum along axis=1 (row-wise sum): [ 6 15 24]

print("\nMean:", np.mean(matrix))
# Output: Mean: 5.0

print("Mean axis=0 (column means):", np.mean(matrix, axis=0))
# Output: Mean axis=0 (column means): [4. 5. 6.]

print("\nMin:", np.min(matrix))
# Output: Min: 1

print("Max:", np.max(matrix))
# Output: Max: 9

print("\nMin axis=1 (min of each row):", np.min(matrix, axis=1))
# Output: Min axis=1 (min of each row): [1 4 7]

print("\nMax axis=0 (max of each column):", np.max(matrix, axis=0))
# Output: Max axis=0 (max of each column): [7 8 9]

print("\nStandard Deviation:", np.std(matrix))
# Output: Standard Deviation: 2.581988897471611

print("\nargmin (index of min):", np.argmin(matrix))
# Output: argmin (index of min): 0

print("argmax (index of max):", np.argmax(matrix))
# Output: argmax (index of max): 8


# ============================================================
# 10. RESHAPING, TRANSPOSE, FLATTEN
# ============================================================

print("\n--- Reshape, Transpose, Flatten ---")
arr = np.arange(1, 13)
print("Original 1D:", arr)
# Output: Original 1D: [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Reshape to 3x4 matrix
matrix = arr.reshape(3, 4)
print("\nReshaped to 3x4:")
print(matrix)
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Reshape to 2x6
print("\nReshaped to 2x6:")
print(arr.reshape(2, 6))
# Output:
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

# Transpose (swap rows and columns)
print("\nTranspose of matrix:")
print(matrix.T)
# Output:
# [[ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]]

# Flatten back to 1D
print("\nFlatten:")
print(matrix.flatten())
# Output: Flatten: [ 1  2  3  4  5  6  7  8  9 10 11 12]


# ============================================================
# 11. STACKING (hstack, vstack)
# ============================================================

print("\n--- Stacking ---")
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

# Horizontal Stack (side by side)
print("hstack (side by side):")
print(np.hstack((a, b)))
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# Vertical Stack (on top of each other)
print("\nvstack (on top of each other):")
print(np.vstack((a, b)))
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Concatenate along axis
print("\nconcatenate axis=0 (vertical):")
print(np.concatenate((a, b), axis=0))
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print("\nconcatenate axis=1 (horizontal):")
print(np.concatenate((a, b), axis=1))
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]


# ============================================================
# 12. SORTING 2D ARRAYS
# ============================================================

print("\n--- Sorting 2D Arrays ---")
matrix = np.array([[3, 1, 2],
                   [6, 4, 5],
                   [9, 7, 8]])

# Sort each row independently
print("Sort each row:")
print(np.sort(matrix))
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Sort along columns (axis=0)
print("\nSort along columns (axis=0):")
print(np.sort(matrix, axis=0))
# Output:
# [[3 1 2]
#  [6 4 5]
#  [9 7 8]]



