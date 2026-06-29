'''
     NumPy
    (Numerical Python):

    - Used for working with arrays.
    - In python we have lists that serve the purpose of arrays, but they are slow to process.
    - NumPy is incredible library to perform mathematical and statistical operations due to Its fast and memory efficient as it
      is optimized to work with latest CPU architectures.
    - NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.So processes can
       access and manipulate them very efficiently.
'''
l = [1, 2, 3, 4, 5]
n = []
for i in l:
    n.append(i * 2)
print(n)


l1 = [1, 8, 9,20]
l2 = [6, 7, 15, 18]

n = []
for i in range(4):
    c = (l1[i] + l2[i])
    n.append(c)
print(n)


l = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
index = [0, 2, 4, 6, 8]

n = []
for i in index:
    n.append(l[i])
print(n)




import numpy as np
l = [1, 2, 3, 4, 5]
n = np.array(l)
mul = n * 2
print(mul)



l1 = [1, 8, 9, 20]
l2 = [6, 7, 15, 18]
n1 = np.array(l1) + np.array(l2)
print(n1)


# 1. Numpy Array 0D
a = np.array(42)
print(a)
# int , float, bool, string if you convert into array it will become 0D array
# and list, tuple, set, dict if you convert into array it will become 1D array

a.ndim 
a.shape 

# priorites of data types in numpy means if any value is float and other is int then it will convert all values into float
# 1. string
# 2. float
# 3. int
# 4. bool
b = np.array([1, 2, 3, 4, 5])
print(b) 

# convert list into array
# convert array into list

# what are the different ways to create numpy array
# ways to create numpy array
 # 1. list to array
 # 2. np.arange()
 # 3. np.random.randint()
 # 4. np.zeros()
 # 5. np.ones()


# Accessing elements / Exracting the values
  # 1. accesing a single value through indexing
       # - positive indexing
       # - negative indexing
  # 2. accesing multiple values based on slicing
       # - positive slicing
       # - negative slicing
  # 3. accesing a multiple value based on indexing
       
  # 4. acessing a mutliple value based on condition
       # - 


# modify the value in numpy 
    # 1. Add or insert , remove or delete, Replace or update
    

# copy array
# sorting the array etc

# Operation 
 # 1. Arithmetic operation
 # 2. comparison operation
 # 3. Mathematical operation
