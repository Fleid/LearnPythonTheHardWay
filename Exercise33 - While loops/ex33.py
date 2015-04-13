# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise33
# -*- coding: utf-8 -*-

numbers = []
numbers_W = []

def numbersAppend(numbersList,maxValue,increment):
	i = 0
	while i < maxValue:
		print "At the top i is %d" % i
		numbersList.append(i)

		i += increment
		print "Numbers now: ", numbersList
		print "At the bottom i is %d" % i


def numbersAppend_W(numbersList,maxValue,increment):
	i = 0
	for i in range(0,maxValue,increment):
		print "W : At the top i is %d" % i
		numbersList.append(i)

		i += increment
		print "W : Numbers now: ", numbersList
		print "W : At the bottom i is %d" % i


numbersAppend(numbers,10,2)
numbersAppend_W(numbers_W,10,2)

print "The numbers, final tally: "

for num in numbers:
	print num

print "The numbers, final tally in W: "

for num in numbers_W:
	print num