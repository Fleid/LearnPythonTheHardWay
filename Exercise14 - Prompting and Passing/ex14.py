# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise14
# -*- coding: utf-8 -*-

from sys import argv
# argv : argument variable, takes argument when the script is called

#unpacking argv
script, user_name, age = argv

prompt = '>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You are %r old.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, age, lives, computer)
