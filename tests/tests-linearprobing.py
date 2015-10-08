# *************************************
#  Example of HashMap Usage
#  Author: Mike Wu
#  Description: Example of how to run
#  the HashMap code.
# *************************************

# Start python and import the file.
from hashmap import *
# Choose a size and Initialize the file.
N = 10
H = HashMap(N)
# 10 random numbers
keys = [23, 142, 120, 1, 24, 32, 69, 6, 34, 21]
# For purposes of an example, just set the values as double the keys.
values = [2*i for i in keys]
# Set everything in the random numbers.
for k, v in zip(keys, values):
  H.set(k, v)

# To get a key.
H.get(23)

# To delete a key.
H.delete(23)

# Print the stored things and summary stats.
print("The load is %f." % H.load())
print("The keys in H: ", H.keys)
print("The values in H: ", H.values)