# *****************************************
#  Fixed-size Hash Map Implementation
#  Author: Mike Wu
#  Description: Uses __hash__
#  with chaining using binary search trees.
# *****************************************

from binarytree import *
class HashMap(object):
  def __init__(self, size):
    self.count = 0
    # This is a fixed size!!!
    self.size = size
    self.stack = [BinarySearchTree() for i in range(size)]

  # Still rely on python for the hash.
  def hashme(self, key):
    return key.__hash__() % self.size

  def set(self, key, value):
    hashvalue = self.hashme(key)
    # If the key already exists, find it and set the value.
    findNode = self.stack[hashvalue].search(key)
    if not findNode is None: # Handle replacement
      findNode.value = value
    else: # The key does not exist, so add its hash (which is always a number) to the tree.
      self.stack[hashvalue].insert(key, value)
      self.count += 1
    # We will always return True here because worst case, we just append it to a list. This has speed problems but by nature of being fixed size, we can't do much about it.
    return True

  def get(self, key):
    hashvalue = self.hashme(key)
    # This defaults None.
    findNode = self.stack[hashvalue].search(key)
    if not findNode is None:
      return findNode.value
    return None

  def delete(self, key):
    hashvalue = self.hashme(key)
    findNode = self.stack[hashvalue].search(key)
    if not findNode is None:
      retval = self.stack[hashvalue].delete(key)
      self.count -= 1
      return retval.value
    return None

  # As with chaining, it is possible to have load factor > 1.
  def load(self):
    if (self.count + self.size == 0): 
      return 0
    return self.count / float(self.size)

  # Python has default __getitem__ and __setitem__ functions.
  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, value):
    return self.set(key, value)

  def __repr__(self):
    return "<HashMap, style:chaining-bst, size:%d>" % self.size 
    