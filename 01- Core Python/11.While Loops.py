'''
Definition: A while loop repeatedly executes a block of code as long as a given condition evaluates to True.
      Execution Order (Mental Flowchart):
        Check condition
          If True → Run indented block → Go back to step 1
          If False → Exit loop → Continue with code after the loop

Execution Flow
1.    Check the condition.
2.    If True → Execute the loop body.
3.    Check the condition again.
4.    Repeat until the condition becomes False.
5.    Exit the loop and continue with the next statement.

Types of While Loop
1.    While Loop: Repeats while the condition is True.
2.    While-Else Loop: else runs only if the loop ends normally (without break).
3.    While True Loop: Creates an infinite loop until stopped using break.
4.    While with if, else, break:
          if → Makes decisions inside the loop.
          else → Executes alternate code inside the loop.
          break → Immediately exits the loop.

Key Point:
While = Check condition → Repeat code while True → Stop when False (or break is used).

'''

# Q1. Write a loop that prints the numbers from 1 to 10, each on a new line.
n = 1
while n <= 10:
    print(n)
    n += 1

# Q2. Write a loop that counts backwards from 10 down to 1, printing each number.
n =  10
while n >= 1:
    print(n)
    n -= 1     

# Q3. Write a loop that prints only the even numbers from 2 to 20 (inclusive).
n = 2
while n % 2 == 0:
    print("even",n)
    if n == 20:
        break
    n += 2

# Q4. Write a loop that calculates the sum of all numbers from 1 to 50. Print the final total at the end.
number= 1
total_sum = 0

while number <= 50:
    total_sum += number
    number += 1
    print(total_sum)
    
# Q5. Write a loop to calculate the factorial of 5 (5 × 4 × 3 × 2 × 1). Print the final result.
factorial = 5
fac_number = 1

while factorial >= 1:
     fac_number *= factorial
     factorial -= 1
     print(fac_number)

# Q6. Check whether Mahesh is available in the class? if available break
while True:
    name = input("Enter the name of student: ")
    if name == "Mahesh":
        print("Mahesh is available in the class.")
        break
    else:
        print(f"{name} is not available in the class. Please try again.")

# Q7. Write a program to print the first 10 multiples of 3 using a while loop.
x = 1
while x <= 10:
    print("DA")
    x = x-5
    if x<-20:
        break

# Q8. Take user input until stop is entered. Store all inputs in one list and unique inputs in another list. Print both lists.
l = []
n1 = []
while True:
    n = input("Enter your category:")
    if n == "stop":
        break
    l.append(n)
    if n not in n1:
        n1.append(n)

print("All categories:", l)
print("Unique categories:", n1)

# Q9. Write a loop that prints the multiplication table of 5 (from 5×1 to 5×10).
n = 1
while n <= 10:
    print(f"5 × {n} = {5 * n}")
    n += 1

# Q10. Write a loop that prints all odd numbers from 1 to 20.
n = 1
while n <= 20:
    if n % 2 != 0:
        print(n)
    n += 1

# Q11. Write a loop that asks the user to guess a number. Stop when the correct number (7) is guessed.
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == 7:
        print("Correct! You guessed the right number.")
        break
    else:
        print("Wrong guess. Try again.")

# Q12. Write a loop that counts how many numbers from 1 to 50 are divisible by 3.
n = 1
count = 0
while n <= 50:
    if n % 3 == 0:
        count += 1
    n += 1
print(f"Total numbers divisible by 3: {count}")

# Q13. Write a loop that prints stars (*) in increasing order from 1 star to 5 stars.
n = 1
while n <= 5:
    print("*" * n)
    n += 1

# Q14. Write a loop that calculates the sum of all odd numbers from 1 to 30.
n = 1
total = 0
while n <= 30:
    if n % 2 != 0:
        total += n
    n += 1
print(f"Sum of odd numbers: {total}")

# Q15. Write a loop that takes user input for a password until the correct password "python123" is entered.
while True:
    password = input("Enter the password: ")
    if password == "python123":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")

# Q16. Write a loop that prints the first 10 natural numbers in reverse order (10 to 1).
n = 10
while n > 0:
    print(n)
    n -= 1


