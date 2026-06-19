# ZeroDivisionError : This error occurs when you try to divide a number by zero. Example : 10 / 0 will raise a ZeroDivisionError because division by zero is undefined in mathematics.
# Boolean as Integer : In Python, the boolean values True and False are treated as integers with values 1 and 0 respectively. This means that you can perform arithmetic operations with boolean values. For example, True + True will result in 2, and False + True will result in 1.
# Comparison operators compare values. Logical operators combine/negate conditions. Identity and membership operators also return boolean results.

'''
Arithmetic Operators
Division & ZeroDivisionError
Operator Precedence
Boolean as Integer
Assignment Operators
Comparison Operators
Chained Comparisons
Logical Operators
Short Circuit Evaluation
Truthy & Falsy Values
Identity Operators
Equality vs Identity
Membership Operators
Membership in Strings
Membership in Collections
Mixed Expressions
'''


'''
# -------------------------------
# Operator Precedence (Common)
# -------------------------------

1. Parentheses                 ()
2. Exponentiation              **
3. Unary Operators             +x, -x, ~x
4. Multiplication              *, /, //, %
5. Addition                    +, -
6. Bitwise Shift               <<, >>
7. Bitwise AND                 &
8. Bitwise XOR                 ^
9. Bitwise OR                  |
10. Comparison / Membership /
    Identity                   == != < <= > >=
                               in, not in
                               is, is not
11. Logical NOT                not
12. Logical AND                and
13. Logical OR                 or
14. Assignment                 = += -= *= /= ...
'''

# ------- OPERATORS --------

# Types of Operators in Python
    
     # 1. Arithmetic Operators : Used to perform mathematical operations on numeric values. Example : +, -, *, /, //, %, ** etc.
        # 2. Assignment Operators : Used to assign values to variables. Example : =, /=, //=, %=, **=, +=, -=, *= etc.
     # 3. Comparison Operators : Used to compare two values and return a boolean result. Example : ==, !=, >, <, >=, <= etc.
     # 4. Logical Operators : Used to combine multiple boolean expressions and return a boolean result. Example : and, or, not etc.
     # 5. Membership Operators : Used to check if a value is present in a sequence (like string, list, tuple, etc.) and return a boolean result. Example : in, not in etc.
     # 6. Identity Operators : Used to compare the memory locations of two objects and return a boolean result. Example : is, is not etc.





# 1. Arithmetic Operators in Python
        # + : Addition operator, used to add two numbers or concatenate two strings. Example : 2 + 3 = 5, "Hello " + "World" = "Hello World"
        # - : Subtraction operator, used to subtract one number from another. Example : 5 - 2 = 3
        # * : Multiplication operator, used to multiply two numbers or repeat a string. Example : 4 * 3 = 12, "Hi! " * 3 = "Hi! Hi! Hi! "
        # / : Division operator, used to divide one number by another and return a float result. Example : 10 / 2 = 5.0
        # // : Floor Division operator, used to divide one number by another and return the largest integer less than or equal to the result. Example : 10 // 3 = 3
        # % : Modulus operator, used to find the remainder when one number is divided by another. Example : 10 % 3 = 1
        # ** : Exponentiation operator, used to raise a number to the power of another. Example : 2 ** 3 = 8

# Arithmetic Operators Precedence in Python
            # Refer to the common Operator Precedence table.


# 2. Assignment Operators in Python
        # = : Assignment operator, used to assign a value to a variable. Example : x = 5
        # += : Add and assign operator, used to add a value to a variable and assign the result back to the variable. Example : x += 3 is equivalent to x = x + 3 
        # -= : Subtract and assign operator, used to subtract a value from a variable and assign the result back to the variable. Example : x -= 2 is equivalent to x = x - 2
        # *= : Multiply and assign operator, used to multiply a value with a variable and assign the result back to the variable. Example : x *= 4 is equivalent to x = x * 4
        # /= : Divide and assign operator, used to divide a variable by a value and assign the result back to the variable. Example : x /= 2 is equivalent to x = x / 2
        # //= : Floor divide and assign operator, used to floor divide a variable by a value and assign the result back to the variable. Example : x //= 3 is equivalent to x = x // 3
        # %= : Modulus and assign operator, used to find the remainder when a variable is divided by a value and assign the result back to the variable. Example : x %= 2 is equivalent to x = x % 2
        # **= : Exponentiate and assign operator, used to raise a variable to the power of a value and assign the result back to the variable. Example : x **= 3 is equivalent to x = x ** 3

# Assignment Operators Precedence in Python
     # Refer to the common Operator Precedence table.



# 3. Comparison Operators in Python
        # == : Equal to operator, used to compare if two values are equal. Example : 5 == 5 is True, "Hello" == "hello" is False
        # != : Not equal to operator, used to compare if two values are not equal. Example : 5 != 3 is True, "Hello" != "Hello" is False
        # > : Greater than operator, used to compare if one value is greater than another. Example : 5 > 3 is True, "b" > "a" is True
        # < : Less than operator, used to compare if one value is less than another.    Example : 5 < 10 is True, "a" < "b" is True
        # >= : Greater than or equal to operator, used to compare if one value is greater than or equal to another. Example : 5 >= 5 is True, 10 >= 5 is True, "b" >= "a" is True
        # <= : Less than or equal to operator, used to compare if one value is less than or equal to another. Example : 5 <= 5 is True, 3 <= 5 is True, "a" <= "b" is True

# Comparison Operators Precedence in Python
       # Refer to the common Operator Precedence table.



# 4. Logical Operators in Python
        # and : Logical AND operator, used to combine two boolean expressions and return True if both expressions are True.
        # or : Logical OR operator, used to combine two boolean expressions and return True if at least one of them is True. Example : True or False is True, False or False is False
        # not : Logical NOT operator, used to negate a boolean expression and return True if the expression is False, and return False if the expression is True. Example : not True is False, not False is True 

# Logical Operators Precedence in Python
      # Refer to the common Operator Precedence table.


# 5. Membership Operators in Python
        # in : Membership operator, used to check if a value is present in a sequence (like string, list, tuple, etc.) and return True if it is present, otherwise return False. Example : 'a' in "Hello" is False, 3 in [1, 2, 3] is True
        # not in : Membership operator, used to check if a value is not present in a sequence (like string, list, tuple, etc.) and return True if it is not present, otherwise return False. Example : 'a' not in "Hello" is True, 4 not in [1, 2, 3] is True    
        

# Membership Operators Precedence in Python    
        # Refer to the common Operator Precedence table.


# 6. Identity Operators in Python
        # is : Identity operator, used to compare the memory locations of two objects and return True if they are the same object, otherwise return False. Example : a = [1, 2, 3]; b = a; a is b is True, a = [1, 2, 3]; b = [1, 2, 3]; a is b is False
        # is not : Identity operator, used to compare the memory locations of two objects and return True if they are not the same object, otherwise return False. Example : a = [1, 2, 3]; b = a; a is not b is False, a = [1, 2, 3]; b = [1, 2, 3]; a is not b is True


# Identity Operators Precedence in Python
        # Refer to the common Operator Precedence table.

        



'''
=====================================================
1. Arithmetic Operators
=====================================================

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus (Remainder)
**  Exponentiation (Power)
'''

# =====================================================
# Addition (+)
# =====================================================

num1 = 10
num2 = 5

addition = num1 + num2                  # Add two numbers
print(addition)                         # 15

float_add = 10.5 + 2.5                  # Float addition
print(float_add)                        # 13.0

string_add = "Hello " + "Python"        # String concatenation
print(string_add)                       # Hello Python

list_add = [1, 2] + [3, 4]              # List concatenation
print(list_add)                         # [1, 2, 3, 4]


# =====================================================
# Subtraction (-)
# =====================================================

subtract = 20 - 8                       # Subtract numbers
print(subtract)                         # 12

negative_result = 5 - 10                # Result can be negative
print(negative_result)                  # -5

float_subtract = 10.5 - 2.5             # Float subtraction
print(float_subtract)                   # 8.0


# =====================================================
# Multiplication (*)
# =====================================================

multiply = 6 * 4                        # Multiply numbers
print(multiply)                         # 24

float_multiply = 2.5 * 4                # Float multiplication
print(float_multiply)                   # 10.0

repeat_string = "Hi " * 3               # Repeat string
print(repeat_string)                    # Hi Hi Hi

repeat_list = [1, 2] * 3                # Repeat list
print(repeat_list)                      # [1, 2, 1, 2, 1, 2]

multiply_zero = 5 * 0                   # Multiply by zero
print(multiply_zero)                    # 0


# =====================================================
# Division (/)
# =====================================================

division = 10 / 2                       # Always returns float
print(division)                         # 5.0

float_division = 7 / 2
print(float_division)                   # 3.5

negative_division = -10 / 2
print(negative_division)                # -5.0

# 10 / 0                               # ZeroDivisionError


# =====================================================
# Floor Division (//)
# =====================================================

floor_division = 10 // 3                # Floor quotient
print(floor_division)                   # 3

negative_floor = -10 // 3               # Floors toward negative infinity
print(negative_floor)                   # -4

float_floor = 10.5 // 2
print(float_floor)                      # 5.0

# 10 // 0                              # ZeroDivisionError


# =====================================================
# Modulus (%)
# =====================================================

remainder = 10 % 3                      # Remainder
print(remainder)                        # 1

even_check = 8 % 2
print(even_check)                       # 0

negative_mod = -10 % 3                  # Sign follows divisor
print(negative_mod)                     # 2

float_mod = 10.5 % 3
print(float_mod)                        # 1.5

# 10 % 0                               # ZeroDivisionError


# =====================================================
# Exponentiation (**)
# =====================================================

power = 2 ** 3                          # 2³
print(power)                            # 8

square = 5 ** 2                         # Square
print(square)                           # 25

cube = 4 ** 3                           # Cube
print(cube)                             # 64

zero_power = 10 ** 0                    # Any number⁰ = 1
print(zero_power)                       # 1

negative_power = 2 ** -2                # Negative exponent
print(negative_power)                   # 0.25

float_power = 9 ** 0.5                  # Square root
print(float_power)                      # 3.0


'''
=====================================================
Corner Cases
=====================================================

10 / 0      -> ZeroDivisionError
10 // 0     -> ZeroDivisionError
10 % 0      -> ZeroDivisionError

5 / 2       -> 2.5
5 // 2      -> 2
5 % 2       -> 1

-10 // 3    -> -4
-10 % 3     -> 2

10 ** 0     -> 1
2 ** -2     -> 0.25
9 ** 0.5    -> 3.0

=====================================================
Return Types

+   -> int, float, str, list
-   -> int, float
*   -> int, float, str, list
/   -> float
//  -> int or float
%   -> int or float
**  -> int or float

=====================================================
Interview Tips

✔ '/' always returns float.
✔ '//' floors toward negative infinity.
✔ '%' returns the remainder.
✔ '**' is exponentiation, not XOR.
✔ Strings and lists support '+' and '*'.
✔ Division, floor division, and modulus by zero raise ZeroDivisionError.
=====================================================
'''





'''
=====================================================
2. Assignment Operators
=====================================================

=    Assignment
+=   Add and Assign
-=   Subtract and Assign
*=   Multiply and Assign
/=   Divide and Assign
//=  Floor Divide and Assign
%=   Modulus and Assign
**=  Exponentiate and Assign
'''

# =====================================================
# Assignment (=)
# =====================================================

num = 10                                # Assign value
print(num)                              # 10

text = "Python"                         # Assign string
print(text)                             # Python

numbers = [1, 2, 3]                     # Assign list
print(numbers)                          # [1, 2, 3]


# =====================================================
# Add and Assign (+=)
# =====================================================

num = 10
num += 5                                # num = num + 5
print(num)                              # 15

text = "Hello"
text += " Python"                       # Concatenate strings
print(text)                             # Hello Python

numbers = [1, 2]
numbers += [3, 4]                       # Extend list
print(numbers)                          # [1, 2, 3, 4]


# =====================================================
# Subtract and Assign (-=)
# =====================================================

num = 20
num -= 8                                # num = num - 8
print(num)                              # 12

num -= 20                               # Result can be negative
print(num)                              # -8


# =====================================================
# Multiply and Assign (*=)
# =====================================================

num = 5
num *= 4                                # num = num * 4
print(num)                              # 20

text = "Hi "
text *= 3                               # Repeat string
print(text)                             # Hi Hi Hi

numbers = [1, 2]
numbers *= 2                            # Repeat list
print(numbers)                          # [1, 2, 1, 2]


# =====================================================
# Divide and Assign (/=)
# =====================================================

num = 10
num /= 2                                # Always returns float
print(num)                              # 5.0

# num /= 0                              # ZeroDivisionError


# =====================================================
# Floor Divide and Assign (//=)
# =====================================================

num = 10
num //= 3                               # Floor quotient
print(num)                              # 3

negative = -10
negative //= 3                          # Floors toward negative infinity
print(negative)                         # -4

# num //= 0                             # ZeroDivisionError


# =====================================================
# Modulus and Assign (%=)
# =====================================================

num = 10
num %= 3                                # Store remainder
print(num)                              # 1

even = 8
even %= 2
print(even)                             # 0

# num %= 0                              # ZeroDivisionError


# =====================================================
# Exponentiate and Assign (**=)
# =====================================================

num = 2
num **= 3                               # num = num ** 3
print(num)                              # 8

square = 5
square **= 2                            # Square
print(square)                           # 25

root = 9
root **= 0.5                            # Square root
print(root)                             # 3.0


'''
=====================================================
Corner Cases
=====================================================

x = 10
x += 5          -> 15

x = "Hi"
x += "!"        -> Hi!

x = [1, 2]
x += [3]        -> [1, 2, 3]

x /= 2          -> Always float

x //= 3         -> Floor division

x %= 2          -> Remainder

x **= 0         -> 1

x /= 0          -> ZeroDivisionError
x //= 0         -> ZeroDivisionError
x %= 0          -> ZeroDivisionError

=====================================================
Return Types

=    -> Assigned value type
+=   -> Depends on operand
-=   -> int or float
*=   -> int, float, str, list
/=   -> float
//=  -> int or float
%=   -> int or float
**=  -> int or float

=====================================================
Interview Tips

✔ x += y is shorthand for x = x + y.
✔ /= always produces a float.
✔ += works with numbers, strings, and lists.
✔ *= can repeat strings and lists.
✔ Assignment operators modify the existing variable.
✔ Division, floor division, and modulus by zero raise ZeroDivisionError.
=====================================================
'''



'''
=====================================================
3. Comparison Operators
=====================================================

==   Equal to
!=   Not Equal to
>    Greater than
<    Less than
>=   Greater than or Equal to
<=   Less than or Equal to
'''

# =====================================================
# Equal To (==)
# =====================================================

equal_numbers = 10 == 10                 # Compare equal numbers
print(equal_numbers)                     # True

equal_strings = "Python" == "Python"     # Compare equal strings
print(equal_strings)                     # True

different_types = 10 == "10"             # Different data types
print(different_types)                   # False

true_equals_one = True == 1              # Boolean as integer
print(true_equals_one)                   # True

false_equals_zero = False == 0           # Boolean as integer
print(false_equals_zero)                 # True


# =====================================================
# Not Equal To (!=)
# =====================================================

not_equal = 10 != 5                      # Values are different
print(not_equal)                         # True

same_value = 5 != 5                      # Same values
print(same_value)                        # False

string_compare = "Python" != "Java"      # Compare strings
print(string_compare)                    # True


# =====================================================
# Greater Than (>)
# =====================================================

greater_number = 10 > 5                  # Number comparison
print(greater_number)                    # True

greater_string = "b" > "a"               # Lexicographical comparison
print(greater_string)                    # True

greater_false = 5 > 10                   # False condition
print(greater_false)                     # False


# =====================================================
# Less Than (<)
# =====================================================

less_number = 5 < 10                     # Number comparison
print(less_number)                       # True

less_string = "apple" < "banana"         # Lexicographical comparison
print(less_string)                       # True

less_false = 10 < 5                      # False condition
print(less_false)                        # False


# =====================================================
# Greater Than or Equal To (>=)
# =====================================================

greater_equal = 10 >= 10                 # Equal values
print(greater_equal)                     # True

greater_value = 15 >= 10                 # Greater value
print(greater_value)                     # True

greater_equal_false = 5 >= 10            # False condition
print(greater_equal_false)               # False


# =====================================================
# Less Than or Equal To (<=)
# =====================================================

less_equal = 10 <= 10                    # Equal values
print(less_equal)                        # True

less_value = 5 <= 10                     # Smaller value
print(less_value)                        # True

less_equal_false = 20 <= 10              # False condition
print(less_equal_false)                  # False


# =====================================================
# Chained Comparisons
# =====================================================

between_range = 10 < 20 < 30             # Both conditions are True
print(between_range)                     # True

outside_range = 10 < 20 > 30             # One condition is False
print(outside_range)                     # False

equal_chain = 5 <= 5 <= 10               # Equal values allowed
print(equal_chain)                       # True


'''
=====================================================
Corner Cases
=====================================================

10 == 10          -> True
10 == "10"        -> False

True == 1         -> True
False == 0        -> True

"a" < "b"         -> True
"apple" < "banana"-> True

5 < 10 < 20       -> True
5 < 10 > 20       -> False

[] == []          -> True
() == ()          -> True

=====================================================
Return Type

All comparison operators return:
bool

=====================================================
Interview Tips

✔ Comparison operators always return True or False.
✔ Strings are compared lexicographically (dictionary order).
✔ True == 1 and False == 0 evaluate to True.
✔ Chained comparisons are allowed (e.g., 1 < x < 10).
✔ == compares values, not memory locations.
=====================================================
'''



'''
=====================================================
4. Logical Operators
=====================================================

and   -> Returns True if both conditions are True
or    -> Returns True if at least one condition is True
not   -> Reverses the boolean result
'''

# =====================================================
# Logical AND (and)
# =====================================================

both_true = True and True                    # Both operands are True
print(both_true)                             # True

one_false = True and False                   # One operand is False
print(one_false)                             # False

both_false = False and False                 # Both operands are False
print(both_false)                            # False

number_and = (10 > 5) and (20 > 15)          # Both conditions are True
print(number_and)                            # True

mixed_and = (10 > 5) and (5 > 20)            # Second condition is False
print(mixed_and)                             # False


# =====================================================
# Logical OR (or)
# =====================================================

both_true = True or True                     # Both operands are True
print(both_true)                             # True

one_true = True or False                     # One operand is True
print(one_true)                              # True

both_false = False or False                  # Both operands are False
print(both_false)                            # False

number_or = (10 > 50) or (20 > 15)           # Second condition is True
print(number_or)                             # True

mixed_or = (10 < 5) or (5 > 20)              # Both conditions are False
print(mixed_or)                              # False


# =====================================================
# Logical NOT (not)
# =====================================================

not_true = not True                          # Reverse True
print(not_true)                              # False

not_false = not False                        # Reverse False
print(not_false)                             # True

not_expression = not (10 > 5)                # Reverse expression result
print(not_expression)                        # False

not_zero = not 0                             # 0 is Falsy
print(not_zero)                              # True

not_number = not 100                         # Non-zero is Truthy
print(not_number)                            # False


# =====================================================
# Logical Operators with Truthy & Falsy Values
# =====================================================

and_string = "Python" and "Java"             # Returns last Truthy value
print(and_string)                            # Java

and_zero = 10 and 0                          # Stops at first Falsy value
print(and_zero)                              # 0

or_string = "" or "Python"                   # Returns first Truthy value
print(or_string)                             # Python

or_numbers = 0 or 100                        # 0 is Falsy
print(or_numbers)                            # 100

or_all_false = "" or [] or 0                 # All values are Falsy
print(or_all_false)                          # 0


# =====================================================
# Short-Circuit Evaluation
# =====================================================

short_and = False and (10 / 0)
# Second expression is NOT evaluated
print(short_and)                             # False

short_or = True or (10 / 0)
# Second expression is NOT evaluated
print(short_or)                              # True


'''
=====================================================
Truthy Values

True
1, 10, -5
"Python"
[1, 2]
(1, 2)
{1, 2}
{"a": 1}

=====================================================
Falsy Values

False
0
0.0
None
''
[]
()
{}
set()

=====================================================
Corner Cases

True and True       -> True
True and False      -> False

True or False       -> True
False or False      -> False

not True            -> False
not False           -> True

10 and 20           -> 20
10 and 0            -> 0

0 or 100            -> 100
"" or "Python"      -> Python

False and (10/0)    -> False
True or (10/0)      -> True

=====================================================
Return Type

With booleans:
    bool

With non-booleans:
    Returns one of the operands

=====================================================
Operator Precedence

not
and
or

=====================================================
Interview Tips

✔ and returns the first Falsy value or the last Truthy value.
✔ or returns the first Truthy value or the last Falsy value.
✔ not always returns a boolean.
✔ Python uses short-circuit evaluation.
✔ Logical operators work with any object, not just booleans.
=====================================================
'''

'''
=====================================================
5. Membership Operators
=====================================================

in       -> Returns True if the value exists
not in   -> Returns True if the value does not exist
'''

# =====================================================
# Membership in Strings
# =====================================================

text = "Hello Python"

contains_python = "Python" in text            # Substring exists
print(contains_python)                        # True

contains_java = "Java" in text                # Substring not found
print(contains_java)                          # False

contains_char = "P" in text                   # Character exists
print(contains_char)                          # True

contains_space = " " in text                  # Space exists
print(contains_space)                         # True

case_sensitive = "python" in text             # Case-sensitive
print(case_sensitive)                         # False


# =====================================================
# Membership in Lists
# =====================================================

numbers = [10, 20, 30, 40]

number_found = 20 in numbers                  # Element exists
print(number_found)                           # True

number_missing = 50 in numbers                # Element not found
print(number_missing)                         # False

not_in_list = 100 not in numbers              # Element absent
print(not_in_list)                            # True


# =====================================================
# Membership in Tuples
# =====================================================

colors = ("Red", "Green", "Blue")

color_found = "Green" in colors               # Value exists
print(color_found)                            # True

color_missing = "Yellow" not in colors        # Value absent
print(color_missing)                          # True


# =====================================================
# Membership in Sets
# =====================================================

fruits = {"Apple", "Banana", "Mango"}

fruit_found = "Apple" in fruits               # Value exists
print(fruit_found)                            # True

fruit_missing = "Orange" in fruits            # Value absent
print(fruit_missing)                          # False


# =====================================================
# Membership in Dictionaries
# =====================================================

student = {
    "name": "John",
    "age": 21,
    "city": "Patna"
}

key_found = "name" in student                 # Checks key
print(key_found)                              # True

key_missing = "salary" in student             # Key not found
print(key_missing)                            # False

value_check = "John" in student.values()      # Check value
print(value_check)                            # True

item_check = ("name", "John") in student.items()  # Check key-value pair
print(item_check)                             # True


# =====================================================
# Membership in Range
# =====================================================

numbers = range(1, 11)

range_found = 5 in numbers                    # Value exists
print(range_found)                            # True

range_missing = 20 not in numbers             # Value absent
print(range_missing)                          # True


# =====================================================
# Empty Collections
# =====================================================

empty_list = []

check_empty = 1 in empty_list                 # Empty collection
print(check_empty)                            # False

empty_string = ""

check_empty_string = "a" in empty_string
print(check_empty_string)                     # False


'''
=====================================================
Corner Cases

"P" in "Python"             -> True
"python" in "Python"        -> False

20 in [10,20,30]            -> True
50 not in [10,20,30]        -> True

"age" in {"age":21}         -> True
21 in {"age":21}            -> False
21 in {"age":21}.values()   -> True

5 in range(1,6)             -> True
6 in range(1,6)             -> False

=====================================================
Return Type

in       -> bool
not in   -> bool

=====================================================
Interview Tips

✔ 'in' checks existence.
✔ 'not in' checks absence.
✔ String membership is case-sensitive.
✔ Dictionary membership checks keys, not values.
✔ Use .values() to check values.
✔ Use .items() to check key-value pairs.
✔ Sets and dictionaries are faster than lists for membership tests.
=====================================================
'''



'''
=====================================================
6. Identity Operators
=====================================================

is      -> Returns True if both variables refer to the same object
is not  -> Returns True if both variables refer to different objects
'''

# =====================================================
# Same Object
# =====================================================

list1 = [1, 2, 3]

list2 = list1                              # Both refer to same object

same_object = list1 is list2
print(same_object)                         # True

not_same_object = list1 is not list2
print(not_same_object)                     # False


# =====================================================
# Different Objects (Same Value)
# =====================================================

list3 = [1, 2, 3]
list4 = [1, 2, 3]

different_object = list3 is list4          # Different memory locations
print(different_object)                    # False

different_memory = list3 is not list4
print(different_memory)                    # True

equal_value = list3 == list4               # Values are equal
print(equal_value)                         # True


# =====================================================
# Identity with Strings
# =====================================================

text1 = "Python"
text2 = "Python"

same_string = text1 is text2               # May be True due to string interning (implementation-dependent)
print(same_string)                         # May be True or False

equal_string = text1 == text2
print(equal_string)                        # True


# =====================================================
# Identity with Numbers
# =====================================================

num1 = 100
num2 = 100

same_number = num1 is num2                 # Often True in CPython due to integer caching (implementation-dependent)
print(same_number)                         # May be True or False

equal_number = num1 == num2
print(equal_number)                        # True


# =====================================================
# Identity with None
# =====================================================

value = None

check_none = value is None                 # Recommended way
print(check_none)                          # True

check_not_none = value is not None
print(check_not_none)                      # False


# =====================================================
# Mutable Objects
# =====================================================

numbers1 = [10, 20]

numbers2 = numbers1

numbers2.append(30)

print(numbers1)                            # [10, 20, 30]
print(numbers2)                            # [10, 20, 30]

same_list = numbers1 is numbers2
print(same_list)                           # True


# =====================================================
# Immutable Objects
# =====================================================

a = 10
b = a

b += 5                                     # Creates a new object

print(a)                                   # 10
print(b)                                   # 15

same_integer = a is b
print(same_integer)                        # False


# =====================================================
# Copy vs Identity
# =====================================================

original = [1, 2, 3]

copied = original.copy()                   # Creates a new object

print(original == copied)                  # True
print(original is copied)                  # False


'''
=====================================================
Corner Cases

[1,2] == [1,2]             -> True
[1,2] is [1,2]             -> False

"Python" == "Python"       -> True
"Python" is "Python"       -> Implementation-dependent (often True in CPython)

100 == 100                 -> True
100 is 100                 -> Implementation-dependent (often True in CPython)

None is None               -> True

=====================================================
Return Type

is      -> bool
is not  -> bool

=====================================================
Time Complexity

is       -> O(1)
is not   -> O(1)

=====================================================
== vs is

==  -> Compares values
is  -> Compares object identity (memory reference)

=====================================================
Interview Tips

✔ Always use 'is None' instead of '== None'.
✔ '==' checks values.
✔ 'is' checks whether two variables point to the same object.
✔ Mutable objects (lists, dicts, sets) usually have different identities.
✔ Strings and small integers may share memory because of Python's interning/caching.
✔ Never use 'is' to compare strings or numbers; use '==' instead.
=====================================================
'''