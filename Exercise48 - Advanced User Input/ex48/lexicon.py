
# -*- coding: utf-8 -*-

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

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
        
        OutputDone = False
        
        # Traitement des nombres
        if isinstance(convert_number(words[x]),int):
            Output.append(('number',convert_number(words[x])))
            OutputDone = True    
         
        # Traitement du lexique           
        else:
            y = 0
            while y < len(Lexicon):
                if words[x].lower() == Lexicon[y][1]:
                    Output.append(Lexicon[y])
                    # On a trouvé, on peut sortir
                    y = len(Lexicon)
                    OutputDone = True
                y+=1
        
        # Sinon c'est une erreur
        if OutputDone == False:
            Output.append(('error',words[x]))
            OutputDone = True
        
    return Output