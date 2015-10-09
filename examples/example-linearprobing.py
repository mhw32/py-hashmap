# *************************************
#  Example of HashMap Usage
#  Author: Mike Wu
#  Description: Example of how to run
#  the linear-probing version of Hashmap.
# *************************************

import probing
# Choose a size and Initialize the file.
N = 5
H = probing.HashMap(N)
# Random strings
keys = ['dog', 'god', 'cat', 'mommy', 'kpcb', 'acceptme', 'foobar']
# For purposes of an example, try to use as varied types as possible.
values = [[1,2,3], 'asd', 12302, probing.HashMap(2), 12, "please", False]
# Notice this is handling conflicts
for k, v in zip(keys, values):
  H.set(k, v)
  print("Hash Load: %f" % H.load()) # Show load changes.

# To get a key.
# Notice that some keys are missing (because size is restricted 5.)
H.get('kpcb')
H.get('acceptme')

# To delete a key.
H.delete('mommy')

# Print the stored things and summary stats.
print("The load is %f." % H.load())
print("The keys in H: ", H.keys)
print("The values in H: ", H.items)