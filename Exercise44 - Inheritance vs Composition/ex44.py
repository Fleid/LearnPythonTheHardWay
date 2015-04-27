# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise44
# -*- coding: utf-8 -*-

#=== Inheritance ===================================#

class Parent(object):

    def override(self):
        print "Parent override()"
        
    def implicit(self):
        print "Parent implicit()"
        
    def altered(self):
        print "Parent altered()"
        
class Child(Parent):

    def override(self):
        print "Child override()"
        
    def altered(self):
        print "Child, Before PARENT altered()"
        super(Child, self).altered()
        print "Child, AFTER PARENT altered()"

dad = Parent()
son = Child()

print "== Inheritace == "
print "-" * 20
dad.implicit()
print "-" * 2
son.implicit()

print "-" * 20
dad.override()
print "-" * 2
son.override()

print "-" * 20
dad.altered()
print "-" * 2
son.altered()

print "-" * 20

#=== Composition ===================================#
class Other(object):

    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
    
    def altered(self):
        print "OTHER altered()"

class Child(object):

	# On va créé une instance un Other à côté de notre instance de Child
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

print "== Composition == "
print "-" * 20
son.implicit()
print "-" * 20
son.override()
print "-" * 20
son.altered()
print "-" * 20