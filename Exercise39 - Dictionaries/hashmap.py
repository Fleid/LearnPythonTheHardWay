# cd ~/Documents/GitHub/LearnPythonTheHardWay/Exercise39
# -*- coding: utf-8 -*-

# On découpe le hashmap en buckets pour des soucis de performances!
	# 1 hashmap fait 256 buckets
	# Chaque clef qu'on insère on l'insère dans un bucket qu'on détermine via un modulo de son hash
	# Dans ce bucket on a N slots, qui sont des couples clef/valeur

# Dans le set, on décide de remplacer la valeur si la clef existe déjà
	# On pourrait choisir d'append dans tous les cas: ce serait lent
	# A la place on pourrait implémenter un troisième niveau de liste qui associe plusieurs valeurs à une clef
	
def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap=[]
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap
	
def hash_key(aMap, key):
	"""Given a key, this will create a number and then convert it to an index for the aMap's buckets."""
	## hash()
	return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	
	## enumerate([])
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
			
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing the existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))
		

def delete(aMAp, key):
	"""Deletes the given key from the Map"""
	bucket = get_bucket(aMap, key)

	#xrange()	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
