''''
 1. Definition & Core Philosophy
        Definition: Conditional statements (also called Control Flow or Decision-Making statements) evaluate whether a condition is True or False. Based on the result, the program executes specific blocks of code.
                The 5 Types of Conditional Statements:
                    if (Execute if condition is True)
                    if-else (Execute one block if True, another if False)
                    if-elif (Check multiple conditions in sequence)
                    if-elif-else (Multiple conditions with a final fallback)
                    nested if (Conditions inside conditions)

                    
 2. The Golden Rule: Block Structure & Indentation
        Before writing a single if statement, you must master Python's block structure. Unlike languages like C++ or Java that use curly braces {}, Python uses indentation (whitespace) to define blocks of code.
                The 3 Rules of Blocks:
                    The Colon (:): Every conditional statement (if, else, elif) MUST end with a colon. This tells Python, "A new block is starting!"
                    The Indentation: The code inside the block must be indented. The standard is 4 spaces (or 1 Tab).
                    The Alignment: Every line inside the same block must be indented equally.
'''







# ============================================================
# 30 BASIC CONDITIONAL STATEMENT PROGRAMS
# ============================================================


# ============================================================
# 1. Check if a number is positive, negative, or zero
# ============================================================
# YOUR CODE HERE:
num = 10
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# ============================================================
# 2. Check if a number is even or odd
# ============================================================
# YOUR CODE HERE:
num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ============================================================
# 3. Find the largest of two numbers
# ============================================================
# YOUR CODE HERE:
a, b = 15, 25
if a > b:
    print(f"{a} is largest")
else:
    print(f"{b} is largest")


# ============================================================
# 4. Find the largest of three numbers
# ============================================================
# YOUR CODE HERE:
a, b, c = 10, 30, 20
if a >= b and a >= c:
    print(f"{a} is largest")
elif b >= a and b >= c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")


# ============================================================
# 5. Check if a person is eligible to vote (age >= 18)
# ============================================================
# YOUR CODE HERE:
age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# ============================================================
# 6. Grade calculator based on marks
# ============================================================
# YOUR CODE HERE:
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


# ============================================================
# 7. Check if a year is a leap year
# ============================================================
# YOUR CODE HERE:
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# ============================================================
# 8. Check if a character is a vowel or consonant
# ============================================================
# YOUR CODE HERE:
char = 'e'
if char in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")


# ============================================================
# 9. Calculate electricity bill based on units
# ============================================================
# YOUR CODE HERE:
units = 150
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print(f"Electricity bill: Rs. {bill}")


# ============================================================
# 10. Check if a number is divisible by 5 and 11
# ============================================================
# YOUR CODE HERE:
num = 55
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")


# ============================================================
# 11. Check triangle validity (sum of angles = 180)
# ============================================================
# YOUR CODE HERE:
a1, a2, a3 = 60, 70, 50
if a1 + a2 + a3 == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")


# ============================================================
# 12. Check if a triangle is equilateral, isosceles, or scalene
# ============================================================
# YOUR CODE HERE:
s1, s2, s3 = 5, 5, 5
if s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# ============================================================
# 13. Calculate profit or loss
# ============================================================
# YOUR CODE HERE:
cost_price, selling_price = 500, 600
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit: Rs. {profit}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss: Rs. {loss}")
else:
    print("No profit, no loss")


# ============================================================
# 14. Check if a number is divisible by 2, 3, or both
# ============================================================
# YOUR CODE HERE:
num = 12
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2 only")
elif num % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Not divisible by 2 or 3")


# ============================================================
# 15. Simple login system
# ============================================================
# YOUR CODE HERE:
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# ============================================================
# 16. Check if a number is between 10 and 50 (inclusive)
# ============================================================
# YOUR CODE HERE:
num = 25
if 10 <= num <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is outside the range")


# ============================================================
# 17. Calculate BMI and give health status
# ============================================================
# YOUR CODE HERE:
weight, height = 70, 1.75  # kg and meters
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"BMI: {bmi:.2f} - Underweight")
elif bmi < 25:
    print(f"BMI: {bmi:.2f} - Normal")
elif bmi < 30:
    print(f"BMI: {bmi:.2f} - Overweight")
else:
    print(f"BMI: {bmi:.2f} - Obese")


# ============================================================
# 18. Discount calculator based on purchase amount
# ============================================================
# YOUR CODE HERE:
amount = 1500
if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.15
elif amount > 1000:
    discount = amount * 0.10
else:
    discount = 0
print(f"Discount: Rs. {discount}, Final: Rs. {amount - discount}")


# ============================================================
# 19. Check if a number is a multiple of 10
# ============================================================
# YOUR CODE HERE:
num = 50
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")


# ============================================================
# 20. Find absolute value without using abs()
# ============================================================
# YOUR CODE HERE:
num = -15
if num < 0:
    absolute = -num
else:
    absolute = num
print(f"Absolute value: {absolute}")


# ============================================================
# 21. Check if a string is empty or not
# ============================================================
# YOUR CODE HERE:
name = "Python"
if name:
    print("String is not empty")
else:
    print("String is empty")


# ============================================================
# 22. Ticket pricing based on age
# ============================================================
# YOUR CODE HERE:
age = 65
if age < 5:
    price = 0
elif age < 18:
    price = 100
elif age < 60:
    price = 200
else:
    price = 150
print(f"Ticket price: Rs. {price}")


# ============================================================
# 23. Check if a number is a perfect square (basic check)
# ============================================================
# YOUR CODE HERE:
num = 25
root = int(num ** 0.5)
if root * root == num:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")


# ============================================================
# 24. Ternary operator - Find max of two numbers
# ============================================================
# YOUR CODE HERE:
a, b = 30, 45
maximum = a if a > b else b
print(f"Maximum is: {maximum}")


# ============================================================
# 25. Check if a list is empty or not
# ============================================================
# YOUR CODE HERE:
my_list = [1, 2, 3]
if len(my_list) == 0:
    print("List is empty")
else:
    print(f"List has {len(my_list)} elements")


# ============================================================
# 26. Nested if - Check age and gender for eligibility
# ============================================================
# YOUR CODE HERE:
age, gender = 25, "M"
if age >= 18:
    if gender == "M":
        print("Male adult")
    else:
        print("Female adult")
else:
    print("Minor")


# ============================================================
# 27. Check if a character is alphabet, digit, or special char
# ============================================================
# YOUR CODE HERE:
char = '7'
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")


# ============================================================
# 28. Convert temperature from Celsius to Fahrenheit or vice versa
# ============================================================
# YOUR CODE HERE:
temp = 37
scale = "C"
if scale == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")
else:
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius}°C")


# ============================================================
# 29. Movie Ticket Pricing with Wednesday Discount
# Movies tickets priced based on age:
#   $12 for adults (18 and over)
#   $8 for children (under 18)
# Everyone gets a $2 discount on Wednesday.
# Hint: Use a variable for day_of_week
# ============================================================
age = 15
day_of_week = "Wednesday"
# YOUR CODE HERE:
price = 12 if age >= 18 else 8

if day_of_week == "Wednesday":
    price -= 2

print(price)

# ============================================================
# 30. Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe, or unripe based on its color.
# Example for Banana:
#   yellow = ripe
#   green = unripe
#   brown = overripe
# ============================================================
fruit = "banana"
color = "yellow"
    # YOUR CODE HERE:
if fruit == "banana":
    if color == "yellow":
        print("Ripe")
    elif color == "green":
        print("Unripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Unknown ripeness")



# ============================================================
# 31. Weather-Based Activity Suggester
# Suggest an activity based on the weather conditions:
#   sunny = go for a walk
#   rainy = stay indoors
#   snowy = build a snowman
#   cloudy = read a book
#   windy = fly a kite
# ============================================================
weather = "rainy"
# YOUR CODE HERE:
if weather == "sunny":
    print("go for a walk")
elif weather == "rainy":
    print("stay indoors")
elif weather == "snowy":
    print("build a snowman")
elif weather == "cloudy":
    print("read a book")
elif weather == "windy":
    print("fly a kite")


# ============================================================
# 32. Transportation Mode Selector
# Choose a mode of transportation based on distance:
#   < 3 miles = walk
#   3-10 miles = bike
#   10-50 miles = car
#   > 50 miles = plane
# ============================================================
distance = 7.5
# YOUR CODE HERE:
if distance < 3:
    print("walk")
elif distance < 10:
    print("bike")
elif distance < 50:
    print("car")
if distance > 50:
    print("plane")


# ============================================================
# 33. Coffee Order Customizer
# Customize a coffee order:
#   Size: "small", "medium", or "large"
#   Option for extra shots of espresso (yes/no)
#   Calculate total price:
#     small = $3, medium = $4, large = $5
#     Each extra shot = $1
# ============================================================
size = "medium"
extra_shots = 2
# YOUR CODE HERE:
if size == "small":
    price = 3
elif size == "medium":
    price = 4
if size == "large":
    price = 5
price += extra_shots * 1
print(price)

