# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise10
# -*- coding: utf-8 -*-

# \n : new line character
# \ : escape sequence
# """...""" : auto escape " and ' and new lines

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# \a		ASCII bell (BEL)
# \f		ASCII formfeed (FF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r ASCII	Carriage Return (CR)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v		ASCII vertical tab (VT)
# \ooo		Character with octal value ooo
# \xhh		Character with hex value hh