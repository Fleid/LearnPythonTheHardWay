# -*- coding: utf-8 -*-

from nose.tools import *
from  ex47.game import Room

# this file must be named BLAH_test.py
# a test function begins with test_
# assert_equal runs test

def test_room():
	# Create an instance of Room(name, description, empty paths)
    gold = Room("GoldRoom",
    			"""This room has gold in it you can grab.
    			There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    
def test_room_paths():

	# Creates 3 instances of Room, no paths
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    
    # Add paths to the center room (K/V in paths)
    center.add_paths({'north':north,'south':south})
    
    # Tests these links
    assert_equal(center.go('north'),north)
    assert_equal(center.go('south'),south)
    
def test_map():

	# Creates 3 instances of Room, no paths
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees","There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    
    # Add paths to all rooms
    start.add_paths({"west": west, "down": down})
    west.add_paths({"east": start})
    down.add_paths({'up' : start})
    
    # Tests these links, and their chaining
    assert_equal(start.go("west"), west)
    assert_equal(start.go("west").go('east'), start)
    assert_equal(start.go("down").go("up"), start)
