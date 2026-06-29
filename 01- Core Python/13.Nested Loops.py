'''
Definition: A nested loop is a loop inside another loop.

Why we use it:
- To print simple grids or repeated real-life data
- To work with rows and columns
- To compare or combine items
- To handle lists inside lists

Important loop ideas used in this file:
- break    : stops the loop early
- continue : skips the current step and moves to the next
- pass     : does nothing, used as a placeholder
- else     : runs only when the loop finishes without break
- append   : adds a value to a list
'''


# Q1. Print 3 rows and 3 seat numbers using nested loops.
for row in range(3):
	for col in range(3):
		print(f"Seat-{row + 1}{col + 1}", end=" ")
	print()


# Q2. Print numbers from 1 to 3 in each row using nested loops.
for row in range(3):
	for col in range(1, 4):
		print(col, end=" ")
	print()


# Q3. Print a simple multiplication table for 2 and 3 using nested loops.
for number in range(2, 4):
	for multiplier in range(1, 6):
		print(f"{number} x {multiplier} = {number * multiplier}")
	print()


# Q4. Print each item from a list of fruits and its first letter using nested loops.
fruits = ["apple", "mango", "grape"]
for fruit in fruits:
	for letter in fruit[:1]:
		print(fruit, "->", letter)


# Q5. Create a list of pairs using nested loops and append.
pairs = []
for left in [1, 2, 3]:
	for right in ["A", "B"]:
		pairs.append((left, right))
print(pairs)


# Q6. Build a 2D list of numbers from 1 to 3 using append.
matrix = []
for row in range(1, 4):
	current_row = []
	for col in range(1, 4):
		current_row.append(col)
	matrix.append(current_row)
print(matrix)


# Q7. Print a small triangle of grocery bag counts using nested loops.
for row in range(1, 6):
	for col in range(row):
		print(f"Bag{col + 1}", end=" ")
	print()


# Q8. Use break in the inner loop to stop when the value becomes 2.
for row in range(1, 4):
	for col in range(1, 5):
		if col == 3:
			break
		print(row, col)


# Q9. Use continue in the inner loop to skip one number.
for row in range(1, 4):
	for col in range(1, 5):
		if col == 2:
			continue
		print(row, col)


# Q10. Use pass inside a nested loop as a placeholder.
for row in range(2):
	for col in range(2):
		pass
print("pass completed")


# Q11. Use loop else clause when the inner loop finishes normally.
for row in range(2):
	for col in range(2):
		print("Row", row, "Col", col)
	else:
		print("Inner loop finished without break")


# Q12. Use break in the inner loop and see that else does not run.
for row in range(2):
	for col in range(3):
		if col == 1:
			break
		print("Row", row, "Col", col)
	else:
		print("This will not print when break happens")


# Q13. Print a grid of coordinates.
for row in range(1, 4):
	for col in range(1, 4):
		print(f"({row}, {col})", end=" ")
	print()


# Q14. Loop through a list of lists and print each number.
numbers = [[1, 2], [3, 4], [5, 6]]
for group in numbers:
	for num in group:
		print(num)


# Q15. Flatten a list of lists using nested loops and append.
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for group in nested_list:
	for num in group:
		flat_list.append(num)
print(flat_list)


# Q16. Print 3 rows and 3 seat numbers using while loops.
row = 1
while row <= 3:
	col = 1
	while col <= 3:
		print(f"Seat-{row}{col}", end=" ")
		col += 1
	print()
	row += 1


# Q17. Print numbers from 1 to 3 in each row using while loops.
row = 1
while row <= 3:
	col = 1
	while col <= 3:
		print(col, end=" ")
		col += 1
	print()
	row += 1


# Q18. Print a small multiplication table using while loops.
number = 2
while number <= 3:
	multiplier = 1
	while multiplier <= 5:
		print(f"{number} x {multiplier} = {number * multiplier}")
		multiplier += 1
	print()
	number += 1


# Q19. Print a triangle of shopping bags using while loops.
row = 1
while row <= 5:
	col = 1
	while col <= row:
		print(f"Bag{col}", end=" ")
		col += 1
	print()
	row += 1


# Q20. Build a list of pairs using while loops and append.
pairs = []
left = 1
while left <= 3:
	right = 1
	while right <= 2:
		pairs.append((left, right))
		right += 1
	left += 1
print(pairs)


# Q21. Print rows and columns using while True and break.
row = 1
while True:
	if row > 3:
		break
	col = 1
	while True:
		if col > 3:
			break
		print(row, col)
		col += 1
	row += 1


# Q22. Print customer tokens in a small triangle using while True loops.
row = 1
while True:
	if row > 3:
		break
	col = 1
	while True:
		if col > row:
			break
		print(f"T{col}", end=" ")
		col += 1
	print()
	row += 1


# Q23. Use while True to count from 1 to 4 in each row.
row = 1
while True:
	if row > 3:
		break
	col = 1
	while True:
		if col > 4:
			break
		print(col, end=" ")
		col += 1
	print()
	row += 1


# Q24. Use while True to print coordinate pairs.
row = 1
while True:
	if row > 2:
		break
	col = 1
	while True:
		if col > 2:
			break
		print(f"({row}, {col})", end=" ")
		col += 1
	print()
	row += 1


# Q25. Flatten a small nested list using while True.
nested_list = [[1, 2], [3, 4]]
flat_list = []
row = 0
while True:
	if row >= len(nested_list):
		break
	col = 0
	while True:
		if col >= len(nested_list[row]):
			break
		flat_list.append(nested_list[row][col])
		col += 1
	row += 1
print(flat_list)



















































































