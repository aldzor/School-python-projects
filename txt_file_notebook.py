# -*- coding: UTF8 -*-

import time

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

try:
	target = open("notebook.txt","r")
	filename = "notebook.txt"
except FileNotFoundError:
	target = open("notebook.txt","w")
	filename = "notebook.txt"
	print("No default notebook was found, created one.")

decider = False
while decider == False:
	print("Now using file",filename)
	print("""\n(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit""")
	operator = operation()
	
	if operator == 1:
		target = open(filename,"r")
		target.seek(0)
		content = target.read()
		print(content)
		target.close()
		
	elif operator == 2:
		target = open(filename,"a")
		content = input("Write a new note: ")
		target.write("\n")
		target.write(content)
		target.write(":::")
		target.write(time.strftime("%X %x"))
		target.close()
		
	elif operator == 3:
		target = open(filename,"w")
		target.close()
		print("Notes deleted.")
		
	elif operator == 4:
		target.close()
		filename = input("Give the name of the new file:")
		try:
			target = open(filename,"r")
		except FileNotFoundError:
			target = open(filename,"w")
			print("No notebook with that name detected, created one.")
	elif operator == 5:
		print("Notebook shutting down, thank you.")
		decider = True
		
	else:
		print("Invalid input")
