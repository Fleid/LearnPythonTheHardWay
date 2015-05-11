# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise45
# -*- coding: utf-8 -*-

class Payload(object):

    def __init__(self,message):
        self.message = message

class EventInput(object):

    def __init__(self):
        pass
    
    def read(self):
        pass
        
class EventOutput(object):

    def __init__(self):
        pass
    
    def write(self):
        pass 
       
class PersistantStorage(object):

    def __init__(self,parameter):
        self.parameter = parameter
    
    def write(self,key,value):
        pass
        
    def read(self,key):
        pass

class CacheStorage(object):

    def __init__(self,parameter):
        self.parameter = parameter
    
    def write(self,key,value):
        pass
        
    def read(self,key):
        pass

class MaterializedView(object):

    def __init__(self,parameter):
        self.parameter = parameter
    
    def write(self,key,value):
        pass

class ETL_01_SK_Generator(object):
    #takes a BK, checks if it exists in the cache, returns that SK or creates one

    def __init__(self):
        pass

class Pipeline_Map(object):

    def __init__(self):
        pass

class Engine(object):

    def __init__(self):
        pass


