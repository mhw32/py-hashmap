# *************************************
#  Example of HashMap Usage
#  Author: Mike Wu
#  Description: Example of how to run
#  the chaining (w/ lists) version of 
#  Hashmap.
# *************************************

import chaining_list as clist
N = 5
H = clist.HashMap(N)
# Random strings
keys = ['dog', 'god', 'cat', 'mommy', 'kpcb', 'acceptme', 'foobar']
# For purposes of an example, try to use as varied types as possible.
values = [[1,2,3], 'asd', 12302, clist.HashMap(2), 12, "please", False]
# Notice that the load here will go over 1 and that is okay.
for k, v in zip(keys, values):
  H.set(k, v)
  print("Hash Load: %f" % H.load()) 

# Retrieve based on keys. Notice here all the keys are stored even though hash is fixed size 5.
H.get('kpcb')
H.get('acceptme')

# To delete a key.
H.delete('mommy')

# Print the stored things and summary stats.
print("The load is %f." % H.load())
print("The keys in H: ", H.keys)
print("The values in H: ", H.items)

