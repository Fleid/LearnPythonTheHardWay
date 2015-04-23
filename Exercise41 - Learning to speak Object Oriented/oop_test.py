# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# Dictionary : {a : aa , b : bb , c : cc}
PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
		"class %%% has-a ___init___ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet, phrase):
	#snippet = question, phrase = answer
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
	
	for sentence in snippet, phrase:
		# copy sentence in result
		result = sentence[:]
		
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
		
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
		
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
	
	return results

# keep going until the hit CTRL-D
try:
	while True:
		# on crée la liste des clefs du dico
		snippets = PHRASES.keys()
		# qu'on mélange, sinon on aurait toujours le même ordre
		random.shuffle(snippets) 
		
		# on parcourt cette liste, clef par clef
		for snippet in snippets:
			# on va chercher la valeur dans le dico associée à la clef
			phrase = PHRASES[snippet]
			# et on génère une question réponse à partir de la fonction
			question, answer = convert(snippet, phrase)
			
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print question
			
			raw_input("> ")
			print "ANSWER : %s\n\n" % answer

except EOFError:
	print "\nBye"