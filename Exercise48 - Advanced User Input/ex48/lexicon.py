
# -*- coding: utf-8 -*-


def scan(sentence):
	
	words = sentence.split()
	
	#Numbers: any string of 0 through 9 characters
	
	Lexicon = [ 
				('stop','the'),
				('stop','in'),
				('stop','of'),
				('stop','from'),
				('stop','at'),
				('stop','it'),
				('direction','north'),
				('direction','south'),
				('direction','east'),
				('direction','west'),
				('direction','down'),
				('direction','up'),
				('direction','left'),
				('direction','right'),
				('direction','back'),
				('verb','go'),
				('verb','stop'),
				('verb','kill'),
				('verb','eat'),
				('noun','door'),
				('noun','bear'),
				('noun','princess'),
				('noun','cabinet')
				]
	
	Output = []
	
	# On peut rester en for, on doit tester tous les mots
	for x in range(0,len(words)):
		y = 0
		while y < len(Lexicon):
		    if Lexicon[y][1] == words[x]:
		        Output.append(Lexicon[y])
		        # On a trouvé, on peut sortir
		        y = len(Lexicon)
		    y+=1
		    
	return Output