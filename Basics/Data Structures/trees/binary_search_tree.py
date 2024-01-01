from typing import Optional, Self

# Operations
#  - Search
#  - Insert
#  - find minValueNode
#  - remove


class TreeNode:
  left: Optional[Self]
  right: Optional[Self]

  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None


def search(root: Optional[TreeNode], target: int) -> bool:
  if not root:
    return False

  if target > root.val:
    return search(root.right, target)
  elif target < root.val:
    return search(root.left, target)
  else:
    return True


def insert(root: Optional[TreeNode], val: int):
  if not root:
    return TreeNode(val)

  if val > root.val:
    root.right = insert(root.right, val)
  elif val < root.val:
    root.left = insert(root.left, val)
  return root


def minValueNode(root: TreeNode) -> TreeNode:
  """
  Return the minimum value node of the BST.
  """
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr


def remove(root: Optional[TreeNode], val: int):
  """
  Remove a node and return the root of the BST.
  """
  if not root:
    return None

  if val > root.val:
    root.right = remove(root.right, val)
  elif val < root.val:
    root.left = remove(root.left, val)
  else:
    if not root.left:
      # Case 1
      return root.right
    elif not root.right:
      # Case 1
      return root.left
    else:
      # Case 2
      minNode = minValueNode(root.right)
      root.val = minNode.val
      root.right = remove(root.right, minNode.val)
  return root
