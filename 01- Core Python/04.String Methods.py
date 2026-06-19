'''
=====================================================
1. String Fundamentals
=====================================================

String Methods Fundamentals
String Immutability
Method Return Types
=====================================================
2. Case Conversion Methods
=====================================================

upper()
lower()
title()
capitalize()
swapcase()
casefold()

=====================================================
3. Whitespace Removal Methods
=====================================================

strip()
lstrip()
rstrip()

=====================================================
4. Searching Methods
=====================================================

find()
rfind()
index()
rindex()

find() vs index()

=====================================================
5. Counting Methods
=====================================================

count()

=====================================================
6. Prefix & Suffix Methods
=====================================================

startswith()
endswith()
removeprefix()
removesuffix()

=====================================================
7. String Validation Methods
=====================================================

String Validation Mastery

isalpha()
isdigit()
isdecimal()
isnumeric()
isalnum()
islower()
isupper()
istitle()
isspace()
isidentifier()
isprintable()
isascii()

=====================================================
8. Splitting & Joining Methods
=====================================================

split()
rsplit()
splitlines()
partition()
rpartition()
join()

split() vs join()
split() vs partition()

=====================================================
9. Replacement & Translation Methods
=====================================================

replace()
translate()
maketrans()

=====================================================
10. String Alignment & Padding
=====================================================

center()
ljust()
rjust()
zfill()

'''

# Difference Between Methods and Functions in Python

     # Function : It executes a specific task and can be called independently. It is not tied to any object or class. Applicable to all data types.
     # Example : print(), len(), type(), input(), int(), float(), str() etc.
     # How to define a function in Python:
     # def function_name(parameters): Used without dot notation.
         


     # Methods : Similar to a function, where it executes a specific task, but it is tied to a specific object or class. It can only be called on that object or class. Applicable to specific data types.
     # Example : upper(), lower(), title(), capitalize(), strip(), find(), index(), count(), startswith(), endswith(), isalpha(), isdigit(), isalnum(), islower(), isupper() etc.
     # How to define a method in Python:
     # variable_name.method_name(parameters) : using dot notation.


# What is the difference between Mutable and Immutable Data Types in Python?

     # Mutable : Values can be modified within the original object. Example : List, Set, Dictionary, etc.
     # How It Works : When you modify a mutable object, you are changing the original object in memory. The variable that references the mutable object reflects the changes because it points to the same memory location.
     # Check Mutability : We can check through the id() function. If the id of the object remains the same after modification, it is mutable.
 

     # Immutable : Values cannot be modified within the original object. Example : String, Tuple, Integer, Float, Boolean, etc.
     # How It Works : When you modify an immutable object, you create a new object in memory. The variable that references the immutable object points to the new memory location where the modified value is stored, while the original variable still points to the original memory location with the original value.
     # Check Immutability : We can check through the id() function. If the id of the object changes after modification, it is immutable.
  



'''
2. Case Conversion Methods
=====================================================

upper()
lower()
title()
capitalize()
swapcase()
casefold()
'''     

text = "Python Programming"

text_upper = text.upper()  # Converts all characters to uppercase
text_lower = text.lower()  # Converts all characters to lowercase
text_title = text.title()  # Converts the first character of each word to uppercase
text_capitalize = text.capitalize()  # Converts the first character to uppercase and the rest to lowercase
text_swapcase = text.swapcase()  # Converts uppercase characters to lowercase and vice versa
text_casefold = text.casefold()  # Converts all characters to lowercase (more aggressive than lower())



'''
3. Whitespace Removal Methods
=====================================================

strip()
lstrip()
rstrip()

'''

text = "   Hello, World!   "
text_strip = text.strip()  # Removes leading(Means: at the beginning) and trailing(Means: at the end) whitespace
text_lstrip = text.lstrip()  # Removes leading whitespace
text_rstrip = text.rstrip()  # Removes trailing whitespace





'''
4. Searching Methods
=====================================================

find()
rfind()
index()
rindex()

find() vs index()

'''

text = "Hello, World! Hello, Python!"
index_find = text.find("Hello")  # Returns the first occurrence index; returns -1 if not found
index_rfind = text.rfind("Hello")  # Returns the last occurrence index; returns -1 if not found
index_index = text.index("Hello")  # Returns the index of the first occurrence of "Hello", raises ValueError if not found
index_rindex = text.rindex("Hello")  # Returns the index of the last occurrence of "Hello", raises ValueError if not found

# rindex() and rfind() are similar, but rindex() raises ValueError if the substring is not found,
# while rfind() returns -1. The "r" means the search starts from the right side.


'''
5. Counting Methods
=====================================================

count()

'''
text = "good Morning, good afternoon, good evening"

count_good = text.count("good")  # Returns the number of occurrences of "good"
count_good_case_sensitive = text.count("Good")  # Returns 0, as "Good" is case-sensitive and not found
count_good_case_insensitive = text.lower().count("good")  # Returns the count of "good" in a case-insensitive manner
count_good_with_start_end = text.count("good", 0, 20)  # Counts occurrences of "good" between index 0 and 20
count_substring = text.count("afternoon")  # Returns the count of "afternoon" in the string


'''
6. Prefix & Suffix Methods
=====================================================

startswith()
endswith()
removeprefix()
removesuffix()
'''
# string.startswith(prefix, start, end) return True if the string starts with the specified prefix, otherwise returns False. The optional start and end parameters can be used to specify a range within the string to check for the prefix.
# string.endswith(suffix, start, end) return True if the string ends with the specified suffix, otherwise returns False. The optional start and end parameters can be used to specify a range within the string to check for the suffix.
# string.removeprefix(prefix) returns a new string with the specified prefix removed if it exists; otherwise, it returns the original string unchanged.
# string.removesuffix(suffix) returns a new string with the specified suffix removed if it exists; otherwise, it returns the original string unchanged.


text = "Furniture Store With Quality Products"

text_startswith = text.startswith("Furniture")  # Returns True, as the string starts with "Furniture"
text_endswith = text.endswith("Products")  # Returns True, as the string ends with "Products"
text_removeprefix = text.removeprefix("Furniture ")  # Removes the prefix "Furniture " from the string
text_removesuffix = text.removesuffix(" Products")  # Removes the suffix " Products" from the string

text_startswith_range = text.startswith("Store", 10, 20)  # Checks if the substring from index 10 to 20 starts with "Store"
text_endswith_range = text.endswith("Quality", 10, 20)  # Checks if the substring from index 10 to 20 ends with "Quality"
text_removeprefix_nonexistent = text.removeprefix("Nonexistent")  # Returns the original string unchanged, as the prefix does not exist
text_removesuffix_nonexistent = text.removesuffix("Nonexistent")  # Returns the original string unchanged, as the suffix does not exist

'''
7. String Validation Methods
=====================================================
    # - Most string validation methods return True only if all relevant characters satisfy the rule.
    # - For empty strings, these methods usually return False (except methods like isascii() and isprintable()).


1. isalpha()       # Checks if all characters are alphabets
2. isdigit()       # Checks if all characters are digits
3. isdecimal()     # Checks if all characters are decimal numbers
4. isnumeric()     # Checks if all characters are numeric
5. isalnum()       # Checks if all characters are alphabets or digits
6. islower()       # Checks if all alphabetic characters are lowercase
7. isupper()       # Checks if all alphabetic characters are uppercase
8. istitle()       # Checks if every word starts with an uppercase letter
9. isspace()       # Checks if all characters are whitespace
10. isidentifier() # Checks if the string is a valid Python identifier
11. isprintable()  # Checks if all characters are printable
12. isascii()      # Checks if all characters are ASCII
'''
# -------------------------------
# isalpha() → Only alphabets
# -------------------------------
"Python".isalpha()        # ✅ True
"Python3".isalpha()       # ❌ False
"Hello World".isalpha()   # ❌ False
"".isalpha()              # ❌ False


# -------------------------------
# isdigit() → Only digit characters
# -------------------------------
"123".isdigit()           # ✅ True
"²".isdigit()             # ✅ True
"12.5".isdigit()          # ❌ False
"-123".isdigit()          # ❌ False


# -------------------------------
# isdecimal() → Only decimal digits (0-9)
# -------------------------------
"123".isdecimal()         # ✅ True
"²".isdecimal()           # ❌ False
"½".isdecimal()           # ❌ False
"12.5".isdecimal()        # ❌ False


# -------------------------------
# isnumeric() → Any numeric character
# -------------------------------
"123".isnumeric()         # ✅ True
"²".isnumeric()           # ✅ True
"½".isnumeric()           # ✅ True
"四".isnumeric()          # ✅ True
"12.5".isnumeric()        # ❌ False


# -------------------------------
# isalnum() → Letters and/or numbers only
# -------------------------------
"Python3".isalnum()       # ✅ True
"ABC123".isalnum()        # ✅ True
"Python!".isalnum()       # ❌ False
"Python 3".isalnum()      # ❌ False


# -------------------------------
# islower() → All letters are lowercase
# -------------------------------
"python".islower()        # ✅ True
"python123".islower()     # ✅ True
"python!".islower()       # ✅ True
"Python".islower()        # ❌ False


# -------------------------------
# isupper() → All letters are uppercase
# -------------------------------
"PYTHON".isupper()        # ✅ True
"PYTHON123".isupper()     # ✅ True
"PYTHON!".isupper()       # ✅ True
"Python".isupper()        # ❌ False


# -------------------------------
# istitle() → Every word starts with uppercase
# -------------------------------
"Hello World".istitle()   # ✅ True
"Python Is Fun".istitle() # ✅ True
"hello World".istitle()   # ❌ False
"Hello world".istitle()   # ❌ False


# -------------------------------
# isspace() → Only whitespace characters
# -------------------------------
"   ".isspace()           # ✅ True
"\t\n".isspace()          # ✅ True
" a ".isspace()           # ❌ False
"".isspace()              # ❌ False


# -------------------------------
# isidentifier() → Valid Python variable name
# -------------------------------
"age".isidentifier()      # ✅ True
"_name".isidentifier()    # ✅ True
"name1".isidentifier()    # ✅ True
"1name".isidentifier()    # ❌ False
"my-name".isidentifier()  # ❌ False


# -------------------------------
# isprintable() → Only printable characters
# -------------------------------
"Hello".isprintable()     # ✅ True
"123".isprintable()       # ✅ True
"Hello\n".isprintable()   # ❌ False
"\t".isprintable()        # ❌ False


# -------------------------------
# isascii() → Only ASCII characters
# -------------------------------
"Python".isascii()        # ✅ True
"123".isascii()           # ✅ True
"!@#$".isascii()          # ✅ True
"ñ".isascii()             # ❌ False
"你好".isascii()          # ❌ False


'''
=====================================================
8. Splitting & Joining Methods
=====================================================

split()       -> Splits from the left
rsplit()      -> Splits from the right
splitlines()  -> Splits at line breaks
partition()   -> Splits at the first occurrence
rpartition()  -> Splits at the last occurrence
join()        -> Joins an iterable into a string
'''

# =====================================================
# split()
# =====================================================

text = "Python Java C++"
split_words = text.split()                    # Default (space)
print(split_words)                            # ['Python', 'Java', 'C++']

csv = "Apple,Banana,Mango"
split_csv = csv.split(",")                    # Custom separator
print(split_csv)                              # ['Apple', 'Banana', 'Mango']

data = "One,Two,Three,Four"
split_limit = data.split(",", 2)              # maxsplit
print(split_limit)                            # ['One', 'Two', 'Three,Four']

single_word = "Python"
split_single = single_word.split(",")         # Separator not found
print(split_single)                           # ['Python']

empty_text = ""
split_empty = empty_text.split()              # Empty string
print(split_empty)                            # []

extra_space = "  Python   Java   C++  "
split_spaces = extra_space.split()            # Ignores extra spaces
print(split_spaces)                           # ['Python', 'Java', 'C++']

empty_values = "A,,B,,C"
split_empty_values = empty_values.split(",")  # Empty elements preserved
print(split_empty_values)                     # ['A', '', 'B', '', 'C']


# =====================================================
# rsplit()
# =====================================================

path = "One,Two,Three,Four"
rsplit_once = path.rsplit(",", 1)             # Split from right
print(rsplit_once)                            # ['One,Two,Three', 'Four']

letters = "A-B-C-D"
rsplit_limit = letters.rsplit("-", 2)         # Right maxsplit
print(rsplit_limit)                           # ['A-B', 'C', 'D']

rsplit_not_found = "Python".rsplit(",")       # Separator not found
print(rsplit_not_found)                       # ['Python']

rsplit_empty = "".rsplit()                    # Empty string
print(rsplit_empty)                           # []


# =====================================================
# splitlines()
# =====================================================

multiline = "Python\nJava\nC++"
lines = multiline.splitlines()                # Remove '\n'
print(lines)                                  # ['Python', 'Java', 'C++']

lines_keep = multiline.splitlines(True)       # Keep '\n'
print(lines_keep)                             # ['Python\n', 'Java\n', 'C++']

single_line = "Python"
single_result = single_line.splitlines()      # No newline
print(single_result)                          # ['Python']

empty_lines = ""
empty_result = empty_lines.splitlines()       # Empty string
print(empty_result)                           # []


# =====================================================
# partition()
# =====================================================

email = "user@gmail.com"
partition_email = email.partition("@")        # First '@'
print(partition_email)                        # ('user', '@', 'gmail.com')

equation = "A=B=C"
partition_equal = equation.partition("=")     # First '='
print(partition_equal)                        # ('A', '=', 'B=C')

partition_not_found = "Python".partition(",") # Separator not found
print(partition_not_found)                    # ('Python', '', '')

# "Python".partition("")                      # ValueError


# =====================================================
# rpartition()
# =====================================================

filepath = "Folder/SubFolder/File.txt"
rpartition_path = filepath.rpartition("/")    # Last '/'
print(rpartition_path)                        # ('Folder/SubFolder', '/', 'File.txt')

math = "A=B=C"
rpartition_equal = math.rpartition("=")       # Last '='
print(rpartition_equal)                       # ('A=B', '=', 'C')

rpartition_not_found = "Python".rpartition(",")
print(rpartition_not_found)                   # ('', '', 'Python')

# "Python".rpartition("")                     # ValueError


# =====================================================
# join()
# =====================================================

languages = ["Python", "Java", "C++"]

space_join = " ".join(languages)              # Space separator
print(space_join)                             # Python Java C++

comma_join = ",".join(languages)              # Comma separator
print(comma_join)                             # Python,Java,C++

hyphen_join = "-".join(languages)             # Hyphen separator
print(hyphen_join)                            # Python-Java-C++

char_join = "-".join("Python")                # Join characters
print(char_join)                              # P-y-t-h-o-n

single_join = ",".join(["Python"])            # Single item
print(single_join)                            # Python

empty_join = ",".join([])                     # Empty iterable
print(empty_join)                             # ''

number_join = ",".join(map(str, [1, 2, 3]))   # Convert numbers first
print(number_join)                            # 1,2,3

# ",".join([1, 2, 3])                         # TypeError


'''
=====================================================
split() vs join()

split()
✔ Input  : String
✔ Output : List

join()
✔ Input  : Iterable of strings
✔ Output : String

=====================================================
split() vs partition()

split()
✔ Returns List
✔ Splits all occurrences

partition()
✔ Returns Tuple
✔ Splits first occurrence only
✔ Keeps separator
'''


'''


=====================================================
9. Replacement & Translation Methods
=====================================================

replace()     -> Replaces substring(s)
translate()   -> Replaces characters using a translation table
maketrans()   -> Creates a translation table
'''

# =====================================================
# replace()
# =====================================================

text = "I love Java"

replace_word = text.replace("Java", "Python")      # Replace a word
print(replace_word)                                # I love Python

sentence = "apple apple apple"

replace_all = sentence.replace("apple", "mango")   # Replace all occurrences
print(replace_all)                                 # mango mango mango

replace_limit = sentence.replace("apple", "mango", 2)  # Replace first 2 only
print(replace_limit)                                   # mango mango apple

replace_not_found = text.replace("C++", "Python")  # Substring not found
print(replace_not_found)                            # I love Java

replace_char = "banana".replace("a", "@")          # Replace character
print(replace_char)                                # b@n@n@

replace_empty = "".replace("a", "b")               # Empty string
print(replace_empty)                               # ''


# =====================================================
# maketrans()
# =====================================================

text = "apple"

translation_table = str.maketrans({
    "a": "@",
    "e": "3"
})                                                  # Create translation table

print(translation_table)
# {97: '@', 101: '3'}

translated_text = text.translate(translation_table)
print(translated_text)                              # @ppl3


# =====================================================
# translate()
# =====================================================

word = "banana"

table = str.maketrans({
    "a": "@",
    "n": "#"
})

translated_word = word.translate(table)
print(translated_word)                              # b@#@#@


# =====================================================
# Remove Characters
# =====================================================

message = "Hello!!!"

remove_table = str.maketrans("", "", "!")          # Remove '!'

removed_text = message.translate(remove_table)
print(removed_text)                                 # Hello


# =====================================================
# Replace Multiple Characters
# =====================================================

password = "P@ssw0rd"

replace_table = str.maketrans({
    "@": "a",
    "0": "o"
})

fixed_password = password.translate(replace_table)
print(fixed_password)                               # Password


# =====================================================
# Separator Not Present
# =====================================================

text = "Python"

replace_missing = text.replace("Java", "C++")
print(replace_missing)                              # Python


# =====================================================
# Empty Translation Table
# =====================================================

text = "Python"

empty_table = str.maketrans({})

same_text = text.translate(empty_table)
print(same_text)                                    # Python


'''
=====================================================
replace() vs translate()

replace()
✔ Replaces substrings
✔ Simple to use
✔ Best for replacing words or phrases

translate()
✔ Replaces individual characters
✔ Uses a translation table
✔ Faster for many character replacements

maketrans()
✔ Creates the translation table used by translate()

=====================================================

Return Types

replace()    -> str
translate()  -> str
maketrans()  -> dict
'''


'''
=====================================================
10. String Alignment & Padding
=====================================================

center()  -> Places the string in the center
ljust()   -> Aligns the string to the left
rjust()   -> Aligns the string to the right
zfill()   -> Pads the string with leading zeros
'''

# =====================================================
# center()
# =====================================================

text = "Python"

center_default = text.center(12)
# Total width = 12, remaining spaces are added equally on both sides
print(center_default)
# '   Python   '

center_star = text.center(12, "*")
# Uses '*' instead of spaces as the fill character
print(center_star)
# '***Python***'

center_equal = text.center(6)
# Width equals string length → No change
print(center_equal)
# 'Python'

center_small = text.center(4)
# Width is smaller than string length → Original string returned
print(center_small)
# 'Python'

# text.center(10, "**")
# TypeError → Fill character must be exactly one character


# =====================================================
# ljust()
# =====================================================

text = "Python"

left_space = text.ljust(10)
# Pads spaces on the right until total width becomes 10
print(left_space)
# 'Python    '

left_dash = text.ljust(10, "-")
# Pads '-' on the right
print(left_dash)
# 'Python----'

left_small = text.ljust(4)
# Width smaller than string length → Original string returned
print(left_small)
# 'Python'

# text.ljust(10, "--")
# TypeError → Fill character must be exactly one character


# =====================================================
# rjust()
# =====================================================

text = "Python"

right_space = text.rjust(10)
# Pads spaces on the left until total width becomes 10
print(right_space)
# '    Python'

right_dash = text.rjust(10, "-")
# Pads '-' on the left
print(right_dash)
# '----Python'

right_small = text.rjust(4)
# Width smaller than string length → Original string returned
print(right_small)
# 'Python'

# text.rjust(10, "--")
# TypeError → Fill character must be exactly one character


# =====================================================
# zfill()
# =====================================================

number = "42"

zero_fill = number.zfill(5)
# Adds leading zeros until total width becomes 5
print(zero_fill)
# '00042'

negative = "-42"

negative_fill = negative.zfill(5)
# Zeros are added after the '-' sign
print(negative_fill)
# '-0042'

positive = "+42"

positive_fill = positive.zfill(5)
# Zeros are added after the '+' sign
print(positive_fill)
# '+0042'

text = "Python"

text_fill = text.zfill(10)
# Works with normal strings too
print(text_fill)
# '0000Python'

already_long = "123456"

long_fill = already_long.zfill(4)
# Width smaller than string length → Original string returned
print(long_fill)
# '123456'

empty = ""

empty_fill = empty.zfill(4)
# Empty string becomes all zeros
print(empty_fill)
# '0000'
