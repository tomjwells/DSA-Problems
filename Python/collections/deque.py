from collections import deque
from typing import Any

# Stands for double-ended-queue

# initialization
list = ["a", "b", "c"]
queue = deque(list)
print(queue)

# Insertion
queue.append("z")
queue.appendleft("g")
print(queue)

# Removal
queue.pop()
queue.popleft()  # This is O(1), the list equivalent would be O(n) (since it is necessary to shift each element over by 1 index)
print(queue)

# Rotation
queue.rotate(-1)
print(queue)

# Extension
queue.extend(["d", "e"])
queue.extendleft(["y", "z"])
print(queue)

# Reverse
queue.reverse()
print(queue)

# Implement a peek operation


def peek(d: deque[Any]):
  item = d.popleft()
  d.appendleft(item)
  return d


# indexing into a deque is slow. Worst case is O(N)
queue[0]  # peek at leftmost item
queue[-1]  # peek at rightmost item

# maxlen - useful to keep a maximum size queue
bounded_deque: deque[int] = deque(maxlen=3)

# Empty the deque
queue.clear()
