'''
 - A dictionary consist 0 to multiple items
 - Each items is key:value
 - Each value is stored in the respective keys
 - Keys can be immutable (int, float, bool, str, tuple)
 - Values can be anything (int, float, bool, str, list, tuple, set, dict)
 - If any 1 value is dict, then it is called Nested dictionary
 - Dictionary is Mutable (where you can add, remove, replace)
 - Indexing can be done in Dictionary 
 - Dictionary Methods :
      - items(), items method return a list of key- value pairs in the dictionary , list of tuple, each tuple consists of (key-value)
      - keys(), keys methods returns a list of keys in the dictionary
      - values(), values methods return a list of values in the dictionary
      - update(), to add single or mutliple items into a dictionary
      - pop(), to delete item in dictionary only using key  or del
      - clear(), clear methods removes all items from the dictionary
      - copy() , copy methods returns a shallow copy of the dictionary, changes to the copy of the dictonary do not affect the original dictionary
      - get() , get method returns the value of the specified key
      - replace the value 
      - replace the item


Definition: A dictionary is an unordered, mutable, and indexed (by key) collection of items in Python, where each item is stored as a key-value pair.

      The 5 Golden Rules of Dictionaries:

            Key-Value Pairs: Every item consists of a key and a value, separated by a colon :.
            Keys must be Immutable (Hashable): Keys can only be integers, floats, booleans, strings, or tuples (if they contain only immutable elements). Lists and sets cannot be keys.
            Keys must be Unique: If you try to add a duplicate key, Python will simply overwrite the old value with the new one.
            Values can be ANYTHING: Values can be numbers, strings, lists, tuples, sets, or even other dictionaries (Nested Dictionaries).
            Mutable: You can add, remove, or change key-value pairs after the dictionary is created.

'''

# 1. Creation & Syntax
# Dictionaries are created using curly braces {} with key-value pairs separated by colons.
# 1. Standard Creation
student = {
    "name": "Rakesh",
    "age": 20,
    "grade": "A"
}
print(student)  # Output: {'name': 'Rakesh', 'age': 20, 'grade': 'A'}

# 2. Empty Dictionary
empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'>

# 3. Using the dict() constructor
# Great for creating dicts from sequences of tuples
coords = dict([("x", 10), ("y", 20)])
print(coords)  # Output: {'x': 10, 'y': 20}

# 4. Duplicate Keys (The Overwrite Rule)
data = {"a": 1, "b": 2, "a": 3}
print(data)  # Output: {'a': 3, 'b': 2} -> The first 'a' was overwritten!



# 2. Accessing Data (Key-Based Lookup)
# Correction from raw notes: We don't use numerical "indexing" (like dict[0]) in dictionaries. Instead, we use key-based lookup.
user = {"name": "Amit", "role": "Admin", "active": True}

# 1. Using Square Brackets [] (Throws KeyError if key is missing!)
print(user["name"])  # Output: Amit
# print(user["age"]) # ❌ KeyError: 'age'

# 2. Using the .get() method (The Safe Way)
# Returns None (or a default value) if the key is missing. No errors!
print(user.get("role"))          # Output: Admin
print(user.get("age"))           # Output: None
print(user.get("age", 18))       # Output: 18 (Returns default if missing)


      # Nested Dictionary Access:
            # When a value is another dictionary, you chain the keys to drill down.

company = {
    "dept": "IT",
    "employee": {
        "id": 101,
        "skills": ["Python", "SQL"]
    }
}

print(company["employee"])             # Output: {'id': 101, 'skills': ['Python', 'SQL']}
print(company["employee"]["id"])       # Output: 101
print(company["employee"]["skills"][0])# Output: Python (Drilling into the list!)


# 3. Modifying Dictionaries (Add, Update, Replace)
# Correction from raw notes: Dictionaries do not have a .replace() method. To "replace" a value, you simply reassign it using the key.
inventory = {"apples": 10, "bananas": 5}

# 1. Adding a NEW key-value pair
inventory["oranges"] = 20
print(inventory)  # Output: {'apples': 10, 'bananas': 5, 'oranges': 20}

# 2. Replacing/Updating an EXISTING value
inventory["apples"] = 50  # Replaces 10 with 50
print(inventory)  # Output: {'apples': 50, 'bananas': 5, 'oranges': 20}

# 3. The update() Method (Adding/Updating multiple items at once)
# If the key exists, it updates the value. If not, it adds a new pair.
inventory.update({"bananas": 100, "grapes": 30})
print(inventory)  # Output: {'apples': 50, 'bananas': 100, 'oranges': 20, 'grapes': 30}



# 4. Removing Elements
data = {"a": 1, "b": 2, "c": 3, "d": 4}

# 1. pop(key): Removes the item with the specified key and RETURNS its value.
removed_val = data.pop("b")
print(removed_val)  # Output: 2
print(data)         # Output: {'a': 1, 'c': 3, 'd': 4}

# 2. popitem(): Removes and returns the LAST inserted key-value pair (as a tuple).
# (In Python 3.7+, dicts maintain insertion order).
last_item = data.popitem()
print(last_item)    # Output: ('d', 4)

# 3. del keyword: Deletes a specific key, or the entire dictionary.
del data["c"]
print(data)         # Output: {'a': 1}

del data            # Deletes the whole dictionary object from memory
# print(data)       # ❌ NameError

# 4. clear(): Empties the dictionary, but keeps the object in memory.
data = {"x": 1, "y": 2}
data.clear()
print(data)         # Output: {}



# 5. Dictionary View Methods (keys, values, items)
# These methods return dynamic view objects (not strict lists). If the dictionary changes, the views reflect those changes immediately.
user = {"name": "Raj", "age": 25, "city": "Mumbai"}

# 1. keys(): Returns all the keys
print(user.keys())    # Output: dict_keys(['name', 'age', 'city'])

# 2. values(): Returns all the values
print(user.values())  # Output: dict_values(['Raj', 25, 'Mumbai'])

# 3. items(): Returns all key-value pairs as tuples
print(user.items())   # Output: dict_items([('name', 'Raj'), ('age', 25), ('city', 'Mumbai')])

# 💡 Pro-Tip: Convert them to actual lists if you need to index them!
keys_list = list(user.keys())
print(keys_list[0])   # Output: name



#  6. Iterating (Looping) Through Dictionaries
scores = {"Math": 90, "Science": 85, "English": 92}

# 1. Loop through KEYS (Default behavior)
for key in scores:
    print(key)  # Output: Math, Science, English

# 2. Loop through VALUES
for value in scores.values():
    print(value)  # Output: 90, 85, 92

# 3. Loop through KEY-VALUE PAIRS (Most common & Pythonic)
for subject, score in scores.items():
    print(f"I scored {score} in {subject}")



# 7. Copying Dictionaries
# Just like lists, using = creates an alias. Use .copy() to create an independent clone.
original = {"a": 1, "b": 2}

# ❌ Aliasing
alias = original
alias["a"] = 99
print(original)  # Output: {'a': 99, 'b': 2} -> Original changed!

# ✅ Shallow Copy
clone = original.copy()
clone["b"] = 50
print(original)  # Output: {'a': 99, 'b': 2} -> Original is safe!


