  # --- FOR LOOP ---
# --- FOR LOOP ---
'''
- LOOPS : Repeating the Code
- FOR : For each value in a sequence
- FOR LOOP : For each value in sequence, repeating the block of code
- SEQUENCE : str, list, tuple, set, dict, range

# 1. LOOP CONTROL STATEMENTS
# break    : Stops the loop immediately.
# continue : Skips the current iteration and moves to the next.
# pass     : Acts as a placeholder for empty code blocks.
# else     : Runs code ONLY if the loop finishes without a break.

'''

# Q1. Write a program to print of first 10 natural numbers using for loop
for i in range(1, 11):
    print(i)

# Q2. Write a program for list of odd numbers from 0 to 20 using for loop

odd_numbers = []
for i in range(0,20):
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)


# Q3. Write a program to print the sum of all numbers in a list using for loop
l = [10, 20, 30, 40, 50]
s = 0
for i in range(len(l)):
    s += l[i]
print(s)


# Q4. Ask user to enter any 5 numbers and sum it using for loop
total = 0
for i in range(5):
    num = eval(input("Enter a number: "))
    total += num
print("The sum of the numbers is:", total)


# Q5. Write a program to print multiplication table 
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Q6. Write a program to give the count of each category
l = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
count = {}
for item in l:
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1
print(count)        
  

# Q7. Write a program to find unique categories 
l = ["M", "M", "F", "M", "F", "M", "F"]
l1 = list(set(l))
for i in l1:
    print(i, l.count(i))

# Q8. Write a program to select akshay
l = ["srk", "akshay", "salman", "srk", "akshay", "salman"]
n = []
for i in l:
    if i == "akshay":
        n.append(i)
        break
print(n)


# Q9. Write a program to print each character of a string using a for loop
s = "Hello, World!"
for i in s:
    print(i)


# Q10. Write a program to find the largest number in a list using a for loop
numbers = [12, 45, 2, 41, 31, 10, 8, 6]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest =  num
print("The largest number is:", largest)
    
# Q11. Write a program to count the number of vowels in a string using a for loop
word = "education"
vowels = "aeiou"
vowel_count = 0
for char in word:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)


# Q12. Write a program to create a new list containing the squares of numbers from an existing list
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n ** 2)
print("Squared list:", squares)


# Q13. Write a program to print only the positive numbers from a list using a for loop
numbers = [-10, 5, -3, 8, 0, -1, 7]
for num in numbers:
    if num > 0:
        print(num)


# Q14. Write a program to calculate the average of numbers in a list using a for loop
marks = [75, 80, 90, 65, 85]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
print("The average is:", average)


# Q15. Write a program to check if a specific name exists in a list using a for loop
names = ["rahul", "priya", "amit", "neha"]
target = "amit"
found = False
for name in names:
    if name == target:
        found = True
        break
        
if found:
    print(f"{target} is in the list.")
else:
    print(f"{target} is not in the list.")


# Q16. Write a program to print the length of each word in a list of strings
words = ["apple", "banana", "kiwi", "mango"]
for word in words:
    print(f"The word '{word}' has {len(word)} letters.")


# Q17. Write a program to sum only the even numbers from a given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers:", even_sum)


# Q18. Write a program to print keys and values of a dictionary using a for loop
student = {"name": "Ravi", "age": 20, "city": "Mumbai"}
for key in student:
    print(key, ":", student[key])