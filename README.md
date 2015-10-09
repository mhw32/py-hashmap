# Hash Map Implementation in Python

Thanks for reading the README!

## Assumptions
In creating this hashmap, the following assumptions were made: 

  1. Only primitives types were used. All objects more advanced were coded in primitive types. 
  2. All keys will be strings and thus have ```__hash__``` python properties.
  3. The hashmap is to be FIXED size. This means that I cannot do things like double the table size to allow for more efficient key,value pair storage. I think this inherently introduces some speed issues. 

## Contents
In this folder, there are three different implementations of a HashMap:

  1. Linear Probing
  2. Chaining w/ Lists
  3. Chaining w/ Binary search trees. (includes a BST implementation)
  4. See ```/examples``` for example scripts on how to run the three different implementations.
  5. See ```/tests``` for simple Unit Tests. This used the ```unittest``` library in Python.

## Implementation Details

Speed wise, chaining offers a lot of benefits over linear probing. For example, chaining is much better at handling collisions. However, one of the instructions provided was that the load should never be greater than one. In the case of chaining, it is indeed possible for the load factor to be greater than one, especially if we have fixed table size.. For example, if I am using linked lists, my lists could be infinitely sized per table entry, making the load factor greater than 1. Therefore I include my linear probing implementation as well. Also notice that for chaining, get() will always return true since even though the table size is fixed, each table entry contains some data structure, whose size is unlimited. 

I've also included two types of chaining in HashMaps. ```chaining_list.py``` stores a list version w/ O(1) setting but O(N) retrieval. ```chaining_bst.py``` stores a binary search tree version w/ O(logN) setting and retrieval. I included both because the case could be made for both as "more optimal".

## End Notes
Feel free to email me ```mike.wu@yale.edu``` if you have any questions or comments. Looking forward to hearing from you!