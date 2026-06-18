# Indexing & Slicing

'''
Sequence Fundamentals
Indexing
Zero-Based Indexing
Negative Indexing
Basic Slicing
Stop Index Exclusion
Slice Defaults
Step Slicing
Advanced Step Patterns
Reverse Slicing
String Indexing & Slicing
List Indexing & Slicing
Tuple Indexing & Slicing
String Immutability
Mutable vs Immutable Sequences
IndexError
Slice Copy Behavior
Real-World String Parsing

'''

# Indexing : Extracting a single character in a string using its position, or extracting a single value/item from an advanced data type using its position.
# Slicing : Extracting multiple characters in a string (which has a pattern), or extracting multiple values/items from an advanced data type (which has a pattern) using positions.


# ----------------------------------------
# How Are Values Stored in Memory?
# ----------------------------------------

# In Python, every value is stored in memory as an object.

'''
Each object has:
1. A value
2. A data type
3. A unique identity (memory address)

When you assign a value to a variable,
Python creates an object in memory and
the variable becomes a reference to that object.

The variable does not store the value directly.
Instead, it points to the object that contains the value.
'''

# Example:

a = 10
f = 12.3
b = True

# Python creates three separate objects in memory:
#
# a ----> 10      (int object)
# f ----> 12.3    (float object)
# b ----> True    (bool object)

# Each variable references its corresponding object.


# ----------------------------------------
# String Objects
# ----------------------------------------

s = "srk"

'''
A string is also stored as a single object in memory.

However, a string contains multiple characters,
and Python allows us to access those characters
individually using indexing and slicing.

Even though we can access individual characters,
the entire string is still stored as one string object.
'''

# Indexing
print(s[0])   # s
print(s[1])   # r
print(s[2])   # k

# Slicing
print(s[0:2]) # sr


# Memory Representation

# s ----> "srk"
#
#           0   1   2
#         +---+---+---+
#         | s | r | k |
#         +---+---+---+
#          -3  -2  -1
# Characters can be accessed using indexes.





# ==============================================================================
# 🧵 INDEXING & SLICING (WITH ALL [::] COMBINATIONS)
# ==============================================================================

text = "data Science"

# ----------------------------------------
# 🗺️ MEMORY REPRESENTATION
# ----------------------------------------
'''
Characters:   d   a   t   a       S   c   i   e   n   c   e
Pos Index:    0   1   2   3   4   5   6   7   8   9  10  11
Neg Index:  -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
'''

# ----------------------------------------
# 1️⃣ INDEXING (Single Character)
# ----------------------------------------
print("--- Indexing ---")
print(text[0])   # 'd' (Positive: 1st character)
print(text[5])   # 'S' (Positive: 6th character)
print(text[-1])  # 'e' (Negative: Last character)
print(text[-7])  # 'S' (Negative: 7th from the end)


# ----------------------------------------
# 2️⃣ SLICING COMBINATIONS [Start : Stop : Step]
# ----------------------------------------
# Rule: 'Start' is INCLUDED, 'Stop' is EXCLUDED. 'Step' is the jump size.
print("\n--- Slicing Combinations ---")

# 1. Default (No colons used, or empty colons)
print(text[:])     # 'data Science' (Same as text[0:12], copies the whole string)
print(text[::])    # 'data Science' (Explicitly showing empty start/stop, default step=1)

# 2. Reversing the String (Negative Step)
print(text[::-1])  # 'ecneicS atad' (Starts from end, goes backward by 1)

# 3. Skipping Characters (Positive Step)
print(text[::2])   # 'dt cec' (Starts at 0, goes to end, jumps by 2)
print(text[1::2])  # 'aaSine' (Starts at index 1, goes to end, jumps by 2)

# 4. Skipping Characters Backward (Negative Step)
print(text[::-2])  # 'eniSaa' (Starts at end, goes backward, jumps by 2)

# 5. Start, Stop, AND Step Combined
print(text[2:8:2]) # 't c' (Starts at 2('t'), stops BEFORE 8('e'), jumps by 2)
print(text[8:2:-1]) # 'eicS a' (Starts at 8('e'), stops BEFORE 2('t'), jumps backward by 1)

print(text[5:4000:1]) # 'Science' (Starts at 5('S'), stops BEFORE 4000, jumps by 1). It works because the stop index is out of range, so it goes to the end of the string without throwing an error.

print(text[-10: -2 : -1])  # '' (Empty string: with a negative step, this start/stop combination does not traverse any characters)
print(text[-1300: -1: 1])  # 'data Scienc' (Starts at -1300, stops BEFORE -1, jumps by 1). It works because the start index is out of range, so it starts from the beginning of the string without throwing an error.
print(text[15:500:1])      # '' (Starts at 15, stops BEFORE 500, jumps by 1). It works because the start index is out of range, so it returns an empty string without throwing an error.

