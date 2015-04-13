# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise36
# -*- coding: utf-8 -*-

# Rules for if-statement
## Every if needs an else
## If the else should never occur, make it die with an error message
## Never nest if more than 2 levels deep

# Rules for loop
## Use while only to loop forever (that's rare)
## Else use for (with range if needed)

from sys import exit


def dead(why):
	print why, "That's so sad!"
	exit(0)

def exterior(waited, stabbed, Inventory):
	if waited and not stabbed:
		action = "#stab"
	elif stabbed:
		action = "#enjoy the moment"
	else:
		action = "#hide"
	print "You are outside of the castle."
	print "You can %s, try the #door or the #window." % action
	
	choice = raw_input("> ")
	
	if choice == "hide" and not waited:
		print "A guard shows up, now what?"
		exterior(True, False, Inventory)
		
	elif choice == "door" and (not waited or stabbed):
		if "Key" in Inventory:
			print "You open the door with the key and enter the castle!"
			interior(Inventory)
		else:
			print "It's locked!"
			exterior(False, False, Inventory)
			
	elif choice == "window" and (not waited or stabbed):
		print "The window is unlocked, you enter the castle!"
		interior(Inventory)
		
	elif choice =="stab" and waited:
		Inventory.append("Key")
		print "You got the key of the door!"
		exterior(True, True, Inventory)
		
	elif waited and not stabbed:
		dead("In front of the guard? Really?")
		
	else: 
		dead("You stumble around the area until you are discovered.")

def interior(Inventory):
	print "Now inside, you can either go to the #kitchen, #upstairs or go back #outside"

	choice = raw_input("> ")
	
	if choice == "kitchen":
		kitchen(Inventory)
	elif choice == "upstairs":
		upstairs(Inventory)
	elif choice == "outside" and "Key" not in Inventory:
		exterior(False,False,Inventory)
	else:
		print "What was that? No interest in doing that"
		interior(Inventory)

def kitchen(Inventory):
	if "Ham" not in Inventory:
		print "You find a ham, and a sleeping cook. You take the ham and back off"
		Inventory.append("Ham")
		interior(Inventory)
	else:
		print "You find the cook awake, and looking for his ham. Once he sees you he rings the alarm!"
		dead("Trying the same thing twice?")
		
def upstairs(Inventory):
	print "You see a huge dog guarding a huge gold chest."
	
	if "Ham" in Inventory and "Key" in Inventory:
		print "You throw the key at the dog, and use the ham on the chest (or the other way around)."
		print "The treasure is yours! Well done!"	
		Inventory.append("Treasure")
		exit(0)
	elif "Ham" in Inventory:
		print "You have the ham to feed the dog, but how will you be able to open the chest?"
		print "Let's go back to find out."
		interior(Inventory)
	elif "Key" in Inventory:
		print "You have the key the open the chest, but how will you be able to distract the dog?"
		print "Let's go back to find out."
		interior(Inventory)
	else:
		print "You were not ready to be here!"
		dead("The dog jumps at you and eat your face.")

def start():
	Inventory = []
	exterior(False, False, Inventory)

start()
