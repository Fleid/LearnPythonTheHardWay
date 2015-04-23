# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise11
# -*- coding: utf-8 -*-

## Virgule pour empêcher print d'envoyer un newline
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
