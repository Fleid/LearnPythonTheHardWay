# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise38
# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	# pop removes the element from the original list when taking it
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Still remaining: ", more_stuff

print "Let's do some things with stuff."

print "stuff[1] : ",  stuff[1]
print "stuff[-1] : ", stuff[-1] # On repart de la fin
print "stuff.pop() : ", stuff.pop() # A noter, pop mange depuis la fin
print ' '.join(stuff)
print '#'.join(stuff[3:5]) # l'énumération exclue la dernière valeur, ici 5

# List useful features:
## Ordered (That doesn't mean sorted)
## Can access items by index (order -1, starts at 0)
## Go through items linearly (from top to bottom)

