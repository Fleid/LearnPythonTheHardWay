# -*- coding: utf-8 -*-

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
    # the get method of dict returns the value linked to the key given in input
        return self.paths.get(direction,None)
        
    def add_paths(self, paths):
    # the update method of dict adds the paths value in input to self.paths
        self.paths.update(paths)
        
    