from collections import OrderedDict

odict: OrderedDict[str, str] = OrderedDict()

odict["key1"] = "value1"
odict["key2"] = "value2"
odict["key3"] = "value3"

print(odict)

# Basic Operations
# Number of Elements
len_odict = len(odict)
print(len_odict)

# If you want to get keys or a particular item, it turns out there is no canonical way.
# Here are some suggestions
keys_as_list = list(odict)
print(keys_as_list[0])

zeroth_item = next(iter(odict))
print(zeroth_item)

# If you want to get the last item, you can do this
last_item = next(reversed(odict))

# popitem is perfect for LRU cache/removing the oldest item
odict.popitem(last=False)
