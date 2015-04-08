# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise08
# -*- coding: utf-8 -*-

## La grille sur laquelle on va projeter des variables
### en %r elle n'est pas typée en entrée!
formatter = "%r %r %r %r"

print formatter % (1,2,3,54)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
)
# A noter: En %r le délimiteur de texte c'est ''
# Sauf si la string contient un ', alors en sortie le délimiteur devient ""

# En prod : toujours %s. Le %r c'est du debug (r pour representation)