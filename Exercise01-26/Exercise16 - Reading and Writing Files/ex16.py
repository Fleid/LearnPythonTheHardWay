# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise16
# -*- coding: utf-8 -*-

# Commands to handle files
## close (file/save)
## read (everything)
## readline
## truncate (cf SQL)
## write ("...")

# option de l'open : http://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w
## r for reading only
## w for writing only (truncate if exists)
## r+ opens for reading and writing (cannot truncate a file)
## w+ for writing and reading (truncate if exists)
## rb+ reading or writing a binary file
## wb+ writing a binary file
## a+ opens for appending

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

## Useless : open en W truncate le fichier. Pour append utiliser a
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n"+ line2 + "\n" + line3 + "\n")

print "And finally, we close it."