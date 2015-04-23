# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise20
# -*- coding: utf-8 -*-

## Function checklist:
#### Does it start with def?
#### Is the name ok? (Only chars and _) 
#### Are arguments correctly defined? With unique names and like (x,y):
#### Is the indentation ok?

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)

# avec %r on a \n qui apparaît, avec %s il est interprété!
# ou alors on supprime le \n naturel du print avec le , mais c'est triché ;)
def print_a_line(line_count, f):
	print "This is line n°%d : %r" % (line_count, f.readline())
	
current_file = open(input_file)

print "First let's print the whole file:"
print_all(current_file)

print "\nNow let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1

print_a_line(current_line, current_file)
current_line += 1

print_a_line(current_line, current_file)
current_line += 1

print_a_line(current_line, current_file)
current_line += 1