# An even better calculator

import math

def asking():
	loop = True
	while loop == True:
		givenNum = input("Give a number:")
		try:
			givenNum = int(givenNum)
			return givenNum
			loop = False
		except Exception:
			print("This input is invalid.")

def operation():
	loop = True
	while loop == True:
		operation = input("Please select something (1-8):")
		try:
			operation = int(operation)
			return operation
			loop = False
		except Exception:
			print("This input is invalid")

print("Calculator")
num1 = asking()
num2 = asking()

decider = False
while decider == False:
	print("""\n(1) +
(2) -
(3) *
(4) /
(5) sin(number1/number2)
(6) cos(number1/number2)
(7) Change numbers
(8) Quit""")
	print("Current numbers:",num1," ",num2)

	operator = operation()

	if operator == 1:
		result = num1 + num2
		print("The result is:",result)
	elif operator == 2:
		result = num1 - num2
		print("The result is:",result)
	elif operator == 3:
		result = num1 * num2
		print("The result is:",result)
	elif operator == 4:
		result = num1 / num2
		print("The result is:",result)
	elif operator == 5:
		result = num1 / num2
		result = math.sin(result)
		print("The result is:",result)
	elif operator == 6:
		result = num1 / num2
		result = math.cos(result)
		print("The result is:",result)
	elif operator == 7:
		num1 = asking()
		num2 = asking()
	elif operator == 8:
		print("Thank you!")
		decider = True
