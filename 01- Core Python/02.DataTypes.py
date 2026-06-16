# Core Foundations

'''
Variables
Data Types
type()
Dynamic Typing
input()
Type Casting
len()
Evaluation Order / Expression Evaluation Order
Lists
Tuples
Sets
Dictionaries
Object References
Mutable vs Immutable
Assignment vs Copying
Shared References
del
Garbage Collection
'''

# Practice Set Related Topics

# OUTPUT IN PYTHON

# -----------------------------------
# print()
# -----------------------------------

# Print a single value
print(12)

# Values can be:
# 1. Integer (without decimal) -> 14, 24, -23
# 2. Float (with decimal)      -> 12.3, 34.2, -23.4
# 3. String (non-numeric)      -> "srk", "da"

# -----------------------------------
# Print multiple values
# -----------------------------------
print(12, 32, 43)

# -----------------------------------
# Separator (sep)
# Used to specify what appears
# between multiple values
# -----------------------------------
print("allu", "arjun", sep=",")

# Output:
# allu,arjun

# -----------------------------------
# Print a single variable
# -----------------------------------
a = 10
print(a)

# -----------------------------------
# Print multiple variables
# -----------------------------------
a = 10
b = 20
print(a, b)

# Output:
# 10 20

# -----------------------------------
# Print a combination of
# variable and value
# -----------------------------------
a = 10
b = 20

print(a, 30)
print(a, b, 30)

# Output:
# 10 30
# 10 20 30




# ----------- Data Types -----------

# In python Data Type will assign automatically based on the value assigned to the variable. This is called Dynamic Programming.

# You can store single value In object --> Fundamental Data Types

    # 1. Integer (without decimal) -> 14, 24, -23
    # 2. Float (with decimal)      -> 12.3, 34.2, -23.4
    # 3. String (non-numeric)      -> "srk",  "da" 
    # 4. Boolean (True/False)      -> True, False

# You can store multiple values in object --> Collection Data Types or Advanced Data Types

    # 1. List 
    # 2. Tuple
    # 3. Set
    # 4. Dictionary


# ----------- type() -----------

# The type() function is used to determine the data type of a variable or value in Python. 
# It returns the type of the object passed as an argument.

type(12)        # Output: <class 'int'>
type(12.3)      # Output: <class 'float'>
type("srk")     # Output: <class 'str'>
type(True)      # Output: <class 'bool'>
type([1, 2, 3]) # Output: <class 'list'>
type((1, 2, 3)) # Output: <class 'tuple'>
type({1, 2, 3}) # Output: <class 'set'>
type({"a": 1})  # Output: <class 'dict'>

# ----------------------------------------
     # len() function is used to determine the length of a string, list, tuple, set, or dictionary in Python.
     # It returns the number of items in the object passed as an argument.
     # len() is not applicable on int, float, and bool data types.
         
len("srk")        # Output: 3  For string, it returns the number of characters in the string.
len([1, 2, 3])    # Output: 3  For list, it returns the number of elements in the list.
len((1, 2, 3))    # Output: 3  For tuple, it returns the number of elements in the tuple.
len({1, 2, 3})    # Output: 3  For set, it returns the number of elements in the set.
len({"a": 1, "b": 2}) # Output: 2 For dictionary, it returns the number of key-value pairs in the dictionary.

# ----------------------------------------
     # id() function is used to get the unique identifier (memory address) of an object in Python.
     # It returns an integer that represents the memory address of the object passed as an argument.
     # Its works for all data types, including int, float, str, list, tuple, set, and dict.

id(12)        # Output: 140711234567456  (The actual output will vary each time the program is run.)   


   
# ----------- Dynamic Typing -----------

# In Python, the data type of a variable is determined automatically based on the value assigned to it. 
# This is called dynamic typing.


# ----------- input() -----------

# The input() function is used to take input from the user in Python. 
# It returns a string containing the user's input.
# By default, the input() function reads input as a string. 
# If you want to convert the input to a different data type, you can use type casting functions like int(), float(), etc.

input("Enter your name: ")
int(input("Enter your age: "))
float(input("Enter your height: "))
eval(input("Enter a Python expression: ")) # eval() function evaluates based on the input and return the result.

# ----------- Type Casting / Conversion -----------

# Type casting is the process of converting a value
# from one data type to another.

# Common type casting functions:
# int()   -> Converts to Integer
# float() -> Converts to Float
# str()   -> Converts to String
# bool()  -> Converts to Boolean (True/False)

# -----------------------------------
# String to Integer
# -----------------------------------
print(int("123"))      # Output: 123

# -----------------------------------
# String to Float
# -----------------------------------
print(float("123.45")) # Output: 123.45

# -----------------------------------
# Integer to String
# -----------------------------------
print(str(123))        # Output: "123"

# -----------------------------------
# Number to Boolean
# -----------------------------------

# 0 always becomes False
print(bool(0))         # Output: False

# Any non-zero number becomes True
print(bool(1))         # Output: True
print(bool(123))       # Output: True
print(bool(-10))       # Output: True

# -----------------------------------
# Float to Boolean
# -----------------------------------

print(bool(0.0))       # Output: False
print(bool(5.6))       # Output: True

# -----------------------------------
# String to Boolean
# -----------------------------------

# Empty string becomes False
print(bool(""))        # Output: False

# Any non-empty string becomes True
print(bool("Hello"))   # Output: True
print(bool("0"))       # Output: True

# -----------------------------------
# Float to Integer
# -----------------------------------

# Decimal part is removed (not rounded)
print(int(12.9))       # Output: 12

# -----------------------------------
# Integer to Float
# -----------------------------------

print(float(25))       # Output: 25.0

# -----------------------------------
# String to Integer and Float
# -----------------------------------

print(int("50"))       # Output: 50
print(float("50"))     # Output: 50.0

# -----------------------------------
# Check Data Type
# -----------------------------------

a = int("100")
print(type(a))         # Output: <class 'int'>

b = float("10.5")
print(type(b))         # Output: <class 'float'>

c = str(200)
print(type(c))         # Output: <class 'str'>

d = bool(1)
print(type(d))         # Output: <class 'bool'>



# ==========================================
# int() Errors
# ==========================================

# "abc" contains letters.
# Python cannot convert letters into a number.
# print(int("abc"))
# ValueError

# "12.5" is a decimal number stored as a string.
# int() expects a whole number string.
# print(int("12.5"))
# ValueError

# Empty string has no value to convert.
# print(int(""))
# ValueError

# List is not a number or numeric string.
# print(int([1, 2, 3]))
# TypeError

# ==========================================
# float() Errors
# ==========================================

# "hello" contains letters.
# Python cannot convert it into a decimal number.
# print(float("hello"))
# ValueError

# Empty string has no numeric value.
# print(float(""))
# ValueError

# Contains numbers and letters together.
# print(float("12.5abc"))
# ValueError

# ==========================================
# Valid Examples
# ==========================================

# String contains a valid whole number.
print(int("123"))      # 123

# String contains a valid decimal number.
print(float("12.5"))   # 12.5

# Number converted into text.
print(str(123))        # '123'

# Non-zero number becomes True.
print(bool(100))       # True


# ----------- Evaluation Order / Expression Evaluation Order -----------

# In python right
# In Python, the evaluation order of expressions is determined by operator precedence and associativity.
# Operator precedence defines the order in which different types of operators are evaluated in an expression.
# The order of evaluation is as follows:
# 1. Parentheses ( )
# 2. Exponentiation **
# 3. Unary plus and minus +x, -x
# 4. Multiplication *, Division /, Floor Division //, Modulus %
# 5. Addition +, Subtraction -
# 6. Comparison Operators ==, !=, >, <, >=, <=
# 7. Logical Operators and, or, not
# Example:
result = 3 + 4 * 2 / (1 - 5) ** 2
print(result)  # Output: 3.5


