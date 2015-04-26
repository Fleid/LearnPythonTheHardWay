# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise43
# -*- coding: utf-8 -*-

'''
* Map
	- next_scene
	- opening_scene
* Engine
	- play
* Scene
	- enter
	* Death
	* Central Corridor
	* Laser Weapon Armory
	* The Bridge
	* Escape Pod
'''

from sys import exit
from random import randint

##===============================================================================##			

class Engine(object):

	def __init__(self, scene_map):
		# On passe le paramètre reçu en entrée en attribut de l'objet, c'est la map qu'on va jouer
		self.scene_map = scene_map
		
	def play(self):
		# on initialise la current sur l'opening (qui a été passée en paramètre du map)
		current_scene = self.scene_map.opening_scene()
		
		# on initialise la dernière sur "finished" en dur
		last_scene = self.scene_map.next_scene('finished')
		
		# on boucle sur les scènes jusqu'à ce que la current vaille la last
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# fin de la scène
		current_scene.enter()

##===============================================================================##
		


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
    	exit(1)


class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):
	def enter(self):
		print 'CentralCorridor'
		action = raw_input("> ")
		return action

class LaserWeaponArmory(Scene):
	def enter(self):
		print 'LaserWeaponArmory'
		action = raw_input("> ")
		return action
		
class TheBridge(Scene):
	def enter(self):
		print 'The Bridge'
		action = raw_input("> ")
		return action

class EscapePod(Scene):
	def enter(self):
		print "Escape Pod"
		action = raw_input("> ")
		return action

class Finished(Scene):
	def enter(self):
		print "You won! Good job."
		return 'finished'

##===============================================================================##		

# On sort la map dans une classe en dehors de l'engine pour faire évoluer les 2 indépendamment
class Map(object):

	# Dictionnaire des scènes
	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death(),
		'finished' : Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		#Retourne la méthode de la scène associée à son nom
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		#Retourne la méthode de la scène d'ouverture
		return self.next_scene(self.start_scene)

##===============================================================================##	

# On initialise la Map, on lui indiquant la première scène en paramètre
a_map = Map("central_corridor")

# On initialise le moteur, en lui passant la map sur laquelle on va jouer
a_game = Engine(a_map)

a_game.play()
