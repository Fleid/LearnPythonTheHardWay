# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise18
# -*- coding: utf-8 -*-

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# the same without *args:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
print_two("Zed", "Shaw")
print_two_again("deZ", "wahS")

test4