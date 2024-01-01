from collections import deque
from typing import Optional, Self


class TreeNode:
  left: Optional[Self]
  right: Optional[Self]

  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None


def bfs(root: TreeNode):
  queue: deque[TreeNode] = deque()

  if root:
    queue.append(root)

  level = 0
  while len(queue) > 0:
    print("level: ", level)
    for _ in range(len(queue)):
      curr = queue.popleft()
      print(curr.val)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    level += 1
