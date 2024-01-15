from typing import List, Self


class TreeNode:
  """
    Definition for a binary tree node.
  """
  val: int
  left: Self
  right: Self

  def __init__(self, val: int, left: Self, right: Self):
    self.val = val
    self.left = left
    self.right = right


def inorder(root: TreeNode):
  """
    Time and space: O(n)
  """
  stack: List[TreeNode] = []
  curr = root

  while curr or stack:
    if curr:
      stack.append(curr)
      curr = curr.left
    else:
      curr = stack.pop()
      print(curr.val)
      curr = curr.right


def preorder(root: TreeNode):
  """
    Time and space: O(n)
  """
  stack: List[TreeNode] = []
  curr = root
  while curr or stack:
    if curr:
      print(curr.val)
      if curr.right:
        stack.append(curr.right)
      curr = curr.left
    else:
      curr = stack.pop()


def postorder(root: TreeNode):
  """
    Time and space: O(n)
  """
  stack = [root]
  visit = [False]
  while stack:
    curr, visited = stack.pop(), visit.pop()
    if curr:
      if visited:
        print(curr.val)
      else:
        # Add the current node to the stack as True, since it has been visited
        stack.append(curr)
        visit.append(True)
        # Add its children to the stack, with False since they have not yet ben visited
        stack.append(curr.right)
        visit.append(False)
        stack.append(curr.left)
        visit.append(False)
