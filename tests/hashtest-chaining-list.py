# **************************************
#  Fixed-size Hash Map Testing
#  Author: Mike Wu
#  Description: Some very basic Unit
#  Tests with Python.
# **************************************

import unittest
import sys
sys.path.append('../')
import chaining_list as clist

# The following tests look at type, collisions, load, and boolean return statements from the tests. Not super comprehensive but good enough.
class HashTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.Hash = clist.HashMap(5)
    # Fill up the Hash w/ string keys
    for i in range(5):
      cls.Hash.set(str(i), i) 
  
  # Test 1 : Make sure that HashMap size is right.
  def test1(self):
    self.assertEqual(self.Hash.size, 5)

  # Test 2 : Make sure that all default correctly.
  def test2a(self): 
    # We can check the lengths of each of the sublists
    self.assertSequenceEqual([0,3,0,0,2], [len(i) for i in self.Hash.keys])
  
  def test2b(self):
    self.assertSequenceEqual([0,3,0,0,2], [len(i) for i in self.Hash.items])
  
  def test2c(self):
    self.assertSequenceEqual([[],['0','2','4'],[],[],['1','3']], self.Hash.keys)

  def test2d(self):
    self.assertSequenceEqual([[],[0,2,4],[],[],[1,3]], self.Hash.items)

  # Test 3 : Make sure that hashme fxn returns an integer less than size.
  def test3a(self):
    self.assertEqual(type(self.Hash.hashme('blah')), int)

  def test3b(self): # integers should work too.
    self.assertEqual(type(self.Hash.hashme('2')), int)

  # Test 4 : Make sure set() should return False (since everything is full and things should conflict). Only works for probing.
  def test4(self):
    self.assertEqual(self.Hash.set('test', 10), True)

  # Test 5 : Make sure that get() on an item is right.
  def test5a(self):
    self.assertEqual(self.Hash.get('2'), 2)
  
  def test5b(self):
    self.assertEqual(self.Hash.get('notexisting'), None)

  # Test 6 : Make sure that delete() on an existing return is right.
  def test6a(self):
    self.assertEqual(self.Hash.delete('3'), 3)

  def test6b(self):
    self.assertEqual(self.Hash.delete('nonexisting'), None)

  #  Test 7 : Load will be greater than 1 here! And should be!
  def test7(self):
    self.Hash.set('6', 6)
    self.assertTrue(self.Hash.load() > 1)

  # Test 8 : Make sure the count is right.
  def test8(self):
    # Things persist so I deleted 3, added test and 6. 
    self.assertEqual(self.Hash.count, 6)

  # Test 9 : Make sure the count decreases after a delete().
  def test9(self):
    self.Hash.delete('1')
    self.assertEqual(self.Hash.count, 5)

if __name__ == '__main__':
    unittest.main()
