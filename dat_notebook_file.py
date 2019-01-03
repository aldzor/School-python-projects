# -*- coding: UTF8 -*-
#simple dat file notebook application

import time
import pickle

def operation():
        loop = True
        while loop == True:
                operation = input("Please select one:")
                try:
                        operation = int(operation)
                        return operation
                        loop = False
                except Exception:
                        print("This input is invalid")
try:
	target = open("notebook.dat","rb")
	
except FileNotFoundError:
	target = open("notebook.dat","wb+")
	print("No default notebook was found, created one.")
	
noteList = []
	
decider = True
while decider == True:
	print("""(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit\n""")
	operator = operation()
		
	if operator == 1:
		for i in noteList:
			print(i)
			
	elif operator == 2:
		addNote = input("Write a new note:")
		noteList.append(addNote+":::"+time.strftime("%X %x"))
		
	elif operator == 3:
		listSize = len(noteList)
		print("The list has",listSize,"notes.")
		noteNumber = int(input("Which of them will be changed?:"))
		print(noteList[noteNumber])
		noteEdit = input("Give  the new note:")
		noteEdit = noteEdit+":::"+time.strftime("%X %x")
		noteList[noteNumber] = noteEdit
			
	elif operator == 4:
		listSize = len(noteList)
		print("The list has",listSize,"notes.")
		noteNumber = int(input("Which of them will be deleted?:"))
		if noteNumber < listSize:
			print("Deleted note",noteList[noteNumber])
			noteList.pop(noteNumber)
		elif noteNumber <= listSize and noteNumber > 0:
			print("Deleted note",noteList[noteNumber-1])
			noteList.pop(noteNumber-1)
		else:
			pass
			
	elif operator == 5:
		target = open("notebook.dat","wb")
		pickle.dump(noteList,target)
		target.close()
		print("Notebook shutting down, thank you.")
		decider = False
			
	else:
		print("Invalid input")
