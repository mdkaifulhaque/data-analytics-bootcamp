'''
Definition: A function is a group of related statements that perform a specific task.
            It takes inputs, processes them, and produces an output.

Why use functions?
      Reusability: Write once, use anywhere.
      Readability: Breaks complex code into smaller, logical chunks.
      Maintainability: If there's a bug, you fix it in one place.

1. TYPES OF FUNCTIONS

      1. Built-in Functions
            Functions that come pre-installed with Python. You don't need to import anything to use them.
            Examples: print(), len(), type(), max(), sum(), input().

      2. User-Defined Functions
            Functions created by the programmer to perform specific, custom tasks.
            Example: A function to calculate the area of a circle.

      3. Module Functions
            Functions that are defined inside a module (a Python file). You must import the module to use them.
            Example: math.sqrt(), random.choice(), datetime.now().
 '''

# 1. FUNCTION SYNTAX & RETURN VALUES

      # A. Function with NO Argument & NO Return Value
      # Takes no input, gives no output (just performs an action).
def greet():
    print("Hello! Welcome to Python.")

greet()  # Output: Hello! Welcome to Python.


      # B. Function with Argument & NO Return Value
      # Takes input, but doesn't return anything
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Rakesh")  # Output: Hello, Rakesh!


      # C. Function with NO Argument & WITH Return Value
      # Takes no input, but calculates and returns a result.
def get_pi():
    return 3.14159

pi_value = get_pi()
print(pi_value)  # Output: 3.14159


      # D. Function with Argument & WITH Return Value
      #The most common type. Takes input, processes it, and returns a result.
def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

result = calculate_area(5)
print(f"Area: {result}")  # Output: Area: 78.5


# 2. FUNCTION ARGUMENTS 

      # A. Compulsory (Required) Arguments
      # Arguments that must be passed. If you miss them, Python throws an error.
def add(a, b):
    return a + b

print(add(5, 10))  # Output: 15
# print(add(5))    # ❌ TypeError: missing 1 required positional argument


      # B. Positional Arguments
      # Arguments passed in the exact order they are defined in the function.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Amit", 25)  # Correct: name="Amit", age=25
introduce(25, "Amit")  # Wrong logic: name=25, age="Amit"

      # C. Keyword Arguments
      # Passing arguments by explicitly naming them. Order doesn't matter!
def introduce(name, age):
    print(f"Name: {name}, Age: {age}")

introduce(age=30, name="Priya")  # Order doesn't matter when using keywords


      # D. Default Arguments
      # Providing a default value in the function definition. If the user doesn't pass it, the default is used.
def greet(name, message="Good morning"):
    print(f"{message}, {name}!")

greet("Rahul")                # Output: Good morning, Rahul!
greet("Rahul", "Good night")  # Output: Good night, Rahul!


      # E. Unlimited Arguments (Arbitrary Arguments)
      # When you don't know how many arguments will be passed.

            # A. *args (Unlimited Positional Arguments)
            # Packs all extra positional arguments into a tuple.
def add_all(*numbers):
    total = sum(numbers)
    return total

print(add_all(1, 2, 3))       # Output: 6
print(add_all(10, 20, 30, 40))# Output: 100            


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=25, city="New York")
# Output:
# name: John
# age: 25
# city: New York
'''
 MODULE
 - A group of function , variables saved to a python file (.py), which is nothing but a module.

      TYPES OF MODULE
      1. Inbuilt Module
      2. User Defined Module
      3. Third Party Module

 VARIOUS POSSIBLE WAYS TO IMPORT MODULE:
      1. import module_name
      2. import module1, module2, module3
      3. import module_name as alias_name
      4. import module 1 as alias1, module2 as alias2
      5. from module import member
      6. from module import member1, member2, member3
      7. from module import member1 as alias1, member2 as alias2
      8. from module import *

  WE CAN ACSESS MEMBERS BY USING MODULE NAME:

  
'''
      # TYPES OF MODULE

# A. Built-in (Inbuilt) Modules
# Modules that come pre-installed with Python's Standard Library.
# Examples: math, random, os, datetime, sys

from ast import If, Import, main
from gettext import install
import math

import pip
print(math.sqrt(16))  # Output: 4.0

# B. User-Defined Modules
# Any Python file you create yourself becomes a module.
# If you create a file named calculator.py with some functions, you can import it into another file.
# File 1: calculator.py

def add(a, b):
    return a + b

PI = 3.14159

# File 2: main.py

import calculator
print(calculator.add(5, 10))
print(calculator.PI)

# C. Third-Party Modules
# Modules created by the community. They do not come with Python. You must install them using pip (Python's package manager).
# Examples: requests, numpy, pandas, flask

# In your terminal/command prompt:
# pip install requests
# In your Python code:
# import requests
# response = requests.get("https://google.com")


      # VARIOUS WAYS TO IMPORT MODULES

# 1. Standard Import
import math
print(math.sqrt(25))

# 2. Import Multiple Modules
import math, random, datetime
print(math.pi)
print(random.randint(1, 10))

# 3. Import with an Alias (Short Name)
import datetime as dt
current_time = dt.datetime.now()
print(current_time)

# 4. Import Multiple Modules with Aliases
import math as m, random as r
print(m.sqrt(16))
print(r.choice(['A', 'B', 'C']))

# 5. Import Specific Member
from math import sqrt
print(sqrt(36))  # No need to write math.sqrt()

# 6. Import Multiple Specific Members
from math import sqrt, pi, pow
print(pi)
print(pow(2, 3))

# 7. Import Specific Members with Aliases
from math import sqrt as s, pi as p
print(s(49))
print(p)

# 8. Import ALL Members (The * Operator)
from math import *
print(sqrt(64))
print(pi)