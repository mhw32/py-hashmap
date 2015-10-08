# **************************************
#  Fixed-size Hash Map Implementation
#  Author: Mike Wu
#  Description: Uses __hash__
#  with chaining for more efficient 
#  storage than linear probing.
# **************************************

# Possible way to make the code more efficient: once the load factor increases beyond a certain threshold, we should double the table length and reorganize the chains. But because our hash must be fixed size, we can't do this.

class HashMap(object):
  def __init__(self, size):
    self.count = 0
    # This is a fixed size!!!
    self.size = size
    self.keys = [[] for i in range(size)]
    self.items = [[] for i in range(size)]

  # Still rely on python for the hash.
  def hashme(self, key):
    return key.__hash__() % self.size

  def rehashme(self, oldhash):
    return (oldhash + 1) % self.size

  def set(self, key, value):
    hashvalue = self.hashme(key)
    returnvalue = False
    # No conflict? Just add it to the list.
    if self.keys[hashvalue] is None: 
      self.keys[hashvalue].append(key)
      self.items[hashvalue].append(value)
      self.count += 1
    else: # There is a conflict.
      # If the key already exists, find it and set the value.
      if key in self.keys[hashvalue]: 
        index = self.keys[hashvalue].index(key)
        self.items[hashvalue][index] = value # Handle replacement.
      else: # The key does not exist, so we can just append it to the bucket it wants to be inside. 
        self.keys[hashvalue].append(key)
        self.items[hashvalue] = value
        self.count += 1
    # We will always return True here because worst case, we just append it to a list. This has speed problems but by nature of being fixed size, we can't do much about it.
    return True

  def get(self, key):
    hashvalue = self.hashme(key)
    # Return None if not in struct.
    myitem = None
    # Check if key is in the bin we think it should be in.
    if key in self.keys[hashvalue]:
      index = self.keys[hashvalue].index(key)
      myitem = self.items[hashvalue][index]
    return myitem

  def delete(self, key):
    hashvalue = self.hashme(key)
    # Return None if not found!
    returnValue = None
    if key in self.keys[hashvalue]:
      # We can use index because key's are unique.
      index = self.keys[hashvalue].index(key)
      returnValue = self.items[hashvalue][index]
      # Pop them from the list of keys and values.
      self.keys[hashvalue].pop(index)
      self.items[hashvalue].pop(index)
      # Record the deletion for load factor. 
      self.count -= 1
    return returnValue

  def load(self):
    if (self.count + self.size == 0): 
      return 0
    return self.count / float(self.size)

  # Python has default __getitem__ and __setitem__ functions.
  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, value):
    return self.set(key, value)







