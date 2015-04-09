# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise17
# -*- coding: utf-8 -*-

# echo "This is a test file." > test.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s... " % (from_file, to_file),

in_file = open(from_file)
out_file = open(to_file, 'w') # write only, truncated on open


out_file.write(in_file.read())

print "Done!"

out_file.close()
in_file.close()