# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise40
# -*- coding: utf-8 -*-

# Getting things from things, all key/value containers, somewhat
## dict style : mystuff['apples']
## module style : import mystuff >> mystuff.apples() || mystuff.tangerine
## class style : thing = MyStuff() >> thing.apples() || thing.tangerine



# le (object) c'est de l'inheritance, pas un paramètre!! voir http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
class Song(object):
	# magic command : __init__
	# magic word : self
	
	# these variables are shared by all instances
	music_style = "python music"
	
	def __init__(self, lyrics):
		# theses variables are local to each instances
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def metallica(self):
		self.lyrics = ["I'm your dream, make your real","I'm your eyes when you must steal"]


happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

print '-' * 10

happy_bday.metallica()
happy_bday.sing_me_a_song()
print happy_bday.music_style