# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise18
# -*- coding: utf-8 -*-

## Function checklist:
#### Does it start with def?
#### Is the name ok? (Only chars and _) 
#### Are arguments correctly defined? With unique names and like (x,y):
#### Is the indentation ok?

## C'est l'indentation qui détermine les limites des définitions
## L'ordre de déclaration n'importe pas

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# the same without *args:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this one just takes one argument

def print_one(arg1):
	print "arg1: %r" % arg1
	print_none()
	print_two_again("deZ", "wahS")

def print_none():
	print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("deZ", "wahS")
print_one("Ring")
print_none()

