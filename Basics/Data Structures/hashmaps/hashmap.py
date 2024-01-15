from typing import List, Optional


class Pair:
  key: str
  val: str

  def __init__(self, key: str, val: str):
    self.key = key
    self.val = val


class HashMap:
  size: int
  capacity: int
  map: List[Optional[Pair]]

  def __init__(self):
    self.size = 0
    self.capacity = 2
    self.map = [None, None]

  def hash(self, key: str):
    index = 0
    for c in key:
      index += ord(c)
    return index % self.capacity

  def get(self, key: str):
    index = self.hash(key)

    while self.map[index] != None:
      pair = self.map[index]
      assert pair is not None
      if pair.key == key:
        return pair.val
      index += 1
      index = index % self.capacity
    return None

  def put(self, key: str, val: str):
    index = self.hash(key)

    while True:
      if self.map[index] == None:
        self.map[index] = Pair(key, val)
        self.size += 1
        if self.size >= self.capacity // 2:
          self.rehash()
        return
      elif self.map[index].key == key:  # type: ignore
        pair = self.map[index]
        assert pair is not None
        pair.val = val
        return

      index += 1
      index = index % self.capacity

  def remove(self, key: str):
    if not self.get(key):
      return

    index = self.hash(key)
    while True:
      if self.map[index].key == key:
        # Removing an element using open-addressing actually causes a bug,
        # because we may create a hole in the list, and our get() may
        # stop searching early when it reaches this hole.
        self.map[index] = None
        self.size -= 1
        return
      index += 1
      index = index % self.capacity

  def rehash(self):
    self.capacity = 2 * self.capacity
    newMap: List[Optional[Pair]] = []
    for _ in range(self.capacity):
      newMap.append(None)

    oldMap = self.map
    self.map = newMap
    self.size = 0
    for pair in oldMap:
      if pair:
        self.put(pair.key, pair.val)

  def print(self):
    for pair in self.map:
      if pair:
        print(pair.key, pair.val)
