
# -*- coding: utf-8 -*-

class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        # We take xxx[1] as in input we have tuples : ('noun','princess')
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None
		
def match(word_list, expecting):
	if word_list:
	    word = word_list.pop(0)
	   
	    if word[0] == expecting:
		    return word
	    else:
			return None
	else:
		return None

def skip(word_list, word_type):
	# Tant qu'on trouve le type dans la liste, on sort le mot
	while peek(word_list) == word_type:
		match(word_list, word_type)

class Parser(object):
	def __init__(self, word_list):
		self.word_list = word_list

	def verb(self):
		skip(self.word_list, 'stop')

		if peek(self.word_list) == 'verb':
			return match(self.word_list, 'verb')
		else:
			raise ParserError("Expected a verb next.")

	def object(self):
		skip(self.word_list, 'stop')
		next_word = peek(self.word_list)

		if next_word == 'noun':
			return match(self.word_list, 'noun')
		elif next_word == 'direction':
			return match(self.word_list, 'direction')
		else:
			raise ParserError("Excepted a noun or a direction next.")

	def subject(self):
		skip(self.word_list, 'stop')
		next_word = peek(self.word_list)

		if next_word == 'noun':
			return match(self.word_list, 'noun')
		elif next_word == 'verb':
			return ('noun','player')
		else:
			raise ParserError("Expected a noun or a verb next.")

def parse_sentence(word_list):
    p = Parser(word_list)
    
    return Sentence(p.subject(), p.verb(), p.object())
