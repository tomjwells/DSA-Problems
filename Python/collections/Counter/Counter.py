from collections import Counter
from typing import Any

c: Counter[Any] = Counter()
c["a"] += 1

# The argument to Counter can be any Python Container (list, set, dict, tuple)
c = Counter("gallad")  # A string can be a container
c = Counter(["a", "b", "c", "d"])
c = Counter({"a": 1, "b": 2})
c = Counter(cats=4, dogs=7)

# Looks like a dict
# Print the elements
print(list(c.elements()))

# String example
c = Counter("abcdeabcdabcaba")  # count elements from a string
c.most_common(3)  # three most common elements
# [('a', 5), ('b', 4), ('c', 3)]
sorted(c)  # list all unique elements
# ['a', 'b', 'c', 'd', 'e']
# Update with argument as any iterable
c.update(("a", "a", "b"))
c.update("aaabbcccdef")
"".join(sorted(c.elements()))  # list elements with repetitions
# 'aaaaabbbbcccdde'
c.values()
# dict_values([5, 4, 3, 2, 1])
sum(c.values())  # total of all counts
# 15
c["a"]  # count of letter 'a'
# 5
for elem in "shazam":  # update counts from an iterable
  c[elem] += 1  # by adding 1 to each element's count
c["a"]  # now there are seven 'a'
# 7
del c["b"]  # remove all 'b'
c["b"]  # now there are zero 'b'
# 0
d = Counter("simsalabim")  # make another counter
c.update(d)  # add in the second counter
c["a"]  # now there are nine 'a'
# 9
c.clear()  # empty the counter
# Note: If a count is set to zero or reduced to zero, it will remain in the counter until the entry is deleted or the counter is cleared:

c = Counter("aaabbc")
c["b"] -= 2  # reduce the count of 'b' by two
c.most_common()  # 'b' is still in, but its count is zero
# [('a', 3), ('c', 1), ('b', 0)]

d = Counter("foobar")

# Counter Arithmetic
sum_counter = c + d
diff_counter = c - d

# Set Operations
intersection = c & d
union = c | d  # max of elements out of both counters
