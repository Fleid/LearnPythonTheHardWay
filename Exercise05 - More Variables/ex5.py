# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise05\ -\ More\ Variables/
# -*- coding: utf-8 -*-

my_name = 'Florian Eiden'
my_age = 35
my_height = 193.5 #cms
my_weight = 110 #kgs
my_eyes = 'Brown'
my_hair = 'Brown'

print "Let's talk about %s." % my_name

print "He's %s cms tall USING S." % my_height # Will cast the float in string
print "He's %d cms tall USING D." % my_height # Will cast the float in int
print "He's %r cms tall USING R." % my_height # Will show the float anyway
print "He's %f cms tall USING F." % my_height # Will show the float in full

print "He's %d kgs heavy." % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)