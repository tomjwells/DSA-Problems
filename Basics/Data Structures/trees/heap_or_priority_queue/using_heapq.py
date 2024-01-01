import heapq
from typing import NamedTuple

lst = []

heapq.heappush(lst, 1)
heapq.heappush(lst, 2)
heapq.heappush(lst, 4)
heapq.heappush(lst, 10)
heapq.heappush(lst, 5)
heapq.heappush(lst, 6)

# heappop - always returns the lowest value until nothing is left
heapq.heappop(lst)


# Usage as a priority queue
# When used as tuples, heapq sorts w.r.t. the first element
lst = []
heapq.heappush(lst, (1, "foo"))
heapq.heappush(lst, (5, "bar"))
heapq.heappush(lst, (3, "baz"))

# Using a Class rather than a Tuple


class QueueItem(NamedTuple):
  priority: int
  work_item: str


lst = []
heapq.heappush(lst, QueueItem(priority=1, work_item="foo"))
heapq.heappush(lst, QueueItem(priority=3, work_item="baz"))
heapq.heappush(lst, QueueItem(priority=2, work_item="womp"))
