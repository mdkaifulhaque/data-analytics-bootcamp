'''
SETS

Sets are used to store multiple unique values in a single variable.
Sets can perform mathematical operations such as Union, Intersection, Difference, and Symmetric Difference.
A set is created using curly braces {} with elements separated by commas.
Sets are unordered collections, meaning elements do not have a fixed position.
Since sets are unordered, indexing and slicing are not supported.
Sets do not allow duplicate values. If duplicate values are provided, they are automatically removed.
Sets can contain only immutable (hashable) objects such as integers, floats, strings, tuples, and booleans.
Nested sets are not allowed because a set itself is mutable.
Sets are mutable objects, which means elements can be added or removed after creation.
Individual elements cannot be modified or replaced directly because indexing is not available.
The + operator cannot be used to concatenate sets.
To combine multiple sets, Union operation is used.
Searching in a set is generally faster than in a list because sets use a hashing mechanism internally.
An empty set is created using set(). Using {} creates an empty dictionary.

  Definition: A set is an unordered, mutable, and unindexed collection of unique, immutable (hashable) elements in Python.
        
    The 5 Golden Rules of Sets:

        Unique: Sets automatically remove duplicates. You cannot have the same value twice.
        Unordered: Elements do not have a fixed position. The order can change every time you access the set.
        Mutable Container: You can add or remove elements from a set after it is created.
        Immutable Elements: The items inside the set must be immutable (hashable).
        Mathematical: Sets natively support powerful mathematical operations like Union and Intersection.
'''

## ---- SET METHODS ---
 
# - for adding a single value we use add() Methods
# - s.update() if we have multiple items 
# - set.discard() , its works same as remove but if its not available its not throw a error
# - set.remove() , remove methods removes the specific elements from the set. if the elements doesn't exist in the set , a key roor is raised.
# - set.clear(), remove all items in the set 
# - del , delte the variable which means object is deleted
# - set.copy(), take a value and create a new object




## ---- SET OPERATION ---
# - set.union() , 
# - set.intersection() , Intersection methods returns a new set with elements that are common to all sets
# - set.isdisjoint() , Isdisjoint methods returns, True if two sets have no itersection, otherwise it returns False
# - set.difference() ,  Difference mehtods returns, a new set with elements in the set that are not in the other specified sets
# - set.symmetric_difference() , symmetric_difference methods returns a new set with elements that are either of the sets, but not in both  (A union B) - (A intersection B)
# - issubset(), issubset methods returns True if all elements of first are available in second set, otherwise it return False
# - issuperset(), issuperset methods return True if all elements of second set are available in first set, otherwise it returns False


# 1. Creating a set
# 1. Standard Creation
s1 = {1, 2, 3, "apple", True}
print(s1)  # Output: {1, 2, 3, 'apple', True} (Order may vary!)

# 2. Automatic Duplicate Removal
s2 = {1, 2, 2, 3, 3, 3}
print(s2)  # Output: {1, 2, 3} -> Duplicates are instantly destroyed!

# 3. THE EMPTY SET TRAP (Classic Interview Question)
empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'> -> {} creates a dictionary!

# ✅ The Fix: Use the set() constructor
empty_set = set()
print(type(empty_set))   # Output: <class 'set'> -> Now it's an empty set!

# 4. Creating from an iterable (List, Tuple, String)
s3 = set([1, 2, 2, 3])   # Output: {1, 2, 3}
s4 = set("hello")        # Output: {'h', 'e', 'l', 'o'} -> Great for finding unique chars!


# 2. The "Hashable" Rule (what can go inside a set?) 
#Because sets use a hashing mechanism internally for lightning-fast lookups, every element inside a set must be hashable (immutable).

# ✅ ALLOWED: Integers, Floats, Strings, Booleans, Tuples
valid_set = {1, 3.14, "Python", True, (10, 20)}
print(valid_set) 

# ❌ NOT ALLOWED: Lists, Dictionaries, and other Sets
# invalid_set = {1, 2, [3, 4]}       # TypeError: unhashable type: 'list'
# invalid_set = {1, 2, {"a": 1}}     # TypeError: unhashable type: 'dict'
# invalid_set = {1, 2, {3, 4}}       # TypeError: unhashable type: 'set'
# NOTE: "Nested sets are not allowed because sets are mutable and therefore unhashable. However, you can use frozenset() (an immutable version of a set) if you absolutely need a set of sets."


# 3. Accessing Elements (The No-Index Rule)
#Because sets are unordered, they do not support indexing or slicing. You cannot ask for "the first element" because there is no first element.
s = {10, 20, 30, 40}

# ❌ CANNOT do this:
# print(s[0])    # TypeError: 'set' object is not subscriptable
# print(s[1:3])  # TypeError: 'set' object is not subscriptable

# ✅ HOW TO ACCESS: Iterate using a for-loop
for item in s:
    print(item)

# ✅ HOW TO CHECK EXISTENCE: Use the 'in' operator (Super fast!)
print(20 in s)   # Output: True



# 4. Modifying Sets: Adding & Removing
# While you can't change an existing element (because you can't index it), you can add new ones or remove existing ones.
# ➕ Adding Elements:
s = {1, 2, 3}

# 1. add(): Adds a SINGLE element
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# 2. update(): Adds MULTIPLE elements from an iterable (list, tuple, string, or another set)
s.update([5, 6])         # Adding from a list
s.update((7, 8), {9, 10}) # Adding from a tuple and another set simultaneously
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# ➖ Removing Elements:
s = {10, 20, 30, 40}

# 1. remove(value): Removes the element. Throws KeyError if not found!
s.remove(20)  
# s.remove(100) # ❌ KeyError: 100

# 2. discard(value): Removes the element. DOES NOT throw an error if not found.
s.discard(30)
s.discard(100)  # ✅ Silently does nothing. (Safer than remove!)

# 3. pop(): Removes and returns a RANDOM element (because sets are unordered!)
removed_item = s.pop()  
print(removed_item)  # Output: 10 (or 40, depending on internal hashing)
print(s)             # Output: {40} (or {10})

# 4. clear(): Empties the entire set
s.clear()
print(s)  # Output: set()

# 5. del: Deletes the set object from memory entirely
del s
# print(s) # ❌ NameError: name 's' is not defined


# 5. Set Operations: Union, Intersection, Difference, Symmetric Difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 1. Union ( | )
# Combines all elements from both sets (removes duplicates).
print(A.union(B))       # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)            # Output: {1, 2, 3, 4, 5, 6, 7, 8}


# 2. Intersection ( & )
# Returns only the elements that are common to both sets.
print(A.intersection(B))  # Output: {4, 5}
print(A & B)              # Output: {4, 5}

# 3. Difference ( - )
# Returns elements in the first set that are not in the second set. (Note: A - B is NOT the same as B - A)
print(A.difference(B))  # Output: {1, 2, 3}  (In A, but not in B)
print(A - B)            # Output: {1, 2, 3}

print(B.difference(A))  # Output: {8, 6, 7}  (In B, but not in A)
print(B - A)            # Output: {8, 6, 7}


# 4. Symmetric Difference ( ^ )
# Returns elements that are in either A or B, but NOT in both. (Essentially: Union minus Intersection).
print(A.symmetric_difference(B))  # Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)                      # Output: {1, 2, 3, 6, 7, 8}



# 6. Set Relationships (Subsets & Supersets)
X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}
Z = {6, 7}

# 1. issubset(): Are ALL elements of X inside Y?
print(X.issubset(Y))      # Output: True
print(X <= Y)             # Output: True (Operator equivalent)

# 2. issuperset(): Does Y contain ALL elements of X?
print(Y.issuperset(X))    # Output: True
print(Y >= X)             # Output: True (Operator equivalent)

# 3. isdisjoint(): Do X and Z have ZERO elements in common?
print(X.isdisjoint(Z))    # Output: True (They share nothing)
print(X.isdisjoint(Y))    # Output: False (They share 1, 2, 3)



# 7. Copying Sets
# Just like lists, using = creates an alias. Use .copy() to create an independent clone.
original = {1, 2, 3}

# ❌ Aliasing
alias = original
alias.add(4)
print(original)  # Output: {1, 2, 3, 4} -> Original changed!

# ✅ Shallow Copy
clone = original.copy()
clone.add(5)
print(original)  # Output: {1, 2, 3, 4} -> Original is safe!
print(clone)     # Output: {1, 2, 3, 4, 5}


# 8. Corner Cases & Common Mistakes
s1 = {1, 2}
s2 = {3, 4}

# print(s1 + s2)  # ❌ TypeError: unsupported operand type(s) for +: 'set' and 'set'

# ✅ The Fix: Use Union
print(s1 | s2)         # Output: {1, 2, 3, 4}
print(s1.union(s2))    # Output: {1, 2, 3, 4}


# 9. Modifying while Iterating
s = {1, 2, 3, 4}
# for item in s:
#     if item == 2:
#         s.remove(item)  # ❌ RuntimeError: Set changed size during iteration

# ✅ The Fix: Iterate over a copy
for item in s.copy():
    if item == 2:
        s.remove(item)



