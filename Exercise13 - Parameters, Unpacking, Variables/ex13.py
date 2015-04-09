# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise13
# -*- coding: utf-8 -*-

# argv : argument variable, it's a module
from sys import argv

# unpacking argv - script seems to be a default mandatory value
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ",second
print "Your third variable is: ",third