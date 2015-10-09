# **************************************
#  Fixed-size Hash Map Testing
#  Author: Mike Wu
#  Description: Some very basic Unit
#  Tests with Python.
# **************************************

import unittest
import sys
sys.path.append('../')
import probing
import chaining_bst as cbst
import chaining_list as clist

# Probing: Expectation [13 /13]
# Linear Chaining: Expectation [11 /13]
# Tree Chaining: Expectation [11 /13]
# We expect some failures for chaining because set() will never return false and load() might be over 1.

# The following tests look at type, collisions, load, and boolean return statements from the tests. Not super comprehensive but good enough.
class HashTest(unittest.TestCase):
  # Define which HashMap we are using
  Hash = probing.HashMap(5)
  # Hash = clist.HashMap(5)
  # Hash = cbst.HashMap(5)
  # Fill up the Hash
  for i in range(5):
    Hash.set(i, i) 

  # Test 1 : Make sure that HashMap size is right.
  def test1(self):
    self.assertEqual(Hash.size, 5)

  # Test 2 : Make sure that all default to None.
  def test2a(self):
    self.assertSequenceEqual([None, None, None, None, None], Hash.keys)
  
  def test2b(self):
    self.assertSequenceEqual([None, None, None, None, None], Hash.items)
      
  # Test 3 : Make sure that hashme fxn returns an integer less than size.
  def test3a(self):
    self.assertEqual(type(Hash.hashme("blah")), int)

  def test3b(self): # integers should work too.
    self.assertEqual(type(Hash.hashme(2)), int)

  # [ MAY FAIL ] Test 4 : Make sure set() should return False (since everything is full and things should conflict). Only works for probing.
  def test4(self):
    self.assertEqual(Hash.set("test", 10), False)

  # Test 5 : Make sure that get() on an item is right.
  def test5a(self):
    self.assertEqual(Hash.get("test"), 10)
  
  def test5b(self):
    self.assertEqual(Hash.get("notexisting"), None)

  # Test 6 : Make sure that delete() on an existing return is right.
  def test6a(self):
    self.assertEqual(Hash.delete("test"), 10)

  def test6b(self):
    self.assertEqual(Hash.delete("nonexisting"), None)

  # [ MAY FAIL ] Test 7 : Make sure that load() is always < 1. Only works for probing. 
  def test7(self):
    Hash.set(6, 6)
    self.assertTrue(Hash.load() < 1)

  # Test 8 : Make sure the count is right.
  def test8(self):
    self.assertEqual(Hash.count, 5)

  # Test 9 : Make sure the count decreases after a delete().
  def test9(self):
    Hash.delete(1)
    self.assertEqual(Hash.count, 4)

if __name__ == '__main__':
    unittest.main()
