#A simple grocery list application

def operation():
	loop = True
	while loop == True:
		operation = input("""Would you like to
(1)Add or
(2)Remove items or
(3)Quit?:""")
		try:
			operation = int(operation)
			return operation
			loop = False
		except Exception:
			print("Incorrect selection")
			
def groceryRemoval():
	operation = input("Which item is deleted?")
	try:
		operation = int(operation)
		return operation
	except Exception:
		print("Incorrect selection.")

decider = True
groceries = []
while decider == True:
	operator = operation()
	
	if operator == 1:
		addedGrocery = input("What will be added?:")
		groceries.append(addedGrocery)
	
	elif operator == 2:
		listSize = len(groceries)
		print("There are",listSize,"items in the list.")
		removedGrocery = groceryRemoval()
		if removedGrocery < listSize:
			groceries.pop(removedGrocery)
		else:
			print("Incorrect selection.")
	
	elif operator == 3:
		print("The following items remain in the list:")
		for i in groceries:
			print(i)
		decider = False
