from typing import Optional, Self


class TreeNode:
  left: Optional[Self]
  right: Optional[Self]

  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None


def inorder(root: Optional[TreeNode]):
  if not root:
    return
  inorder(root.left)
  print(root.val)
  inorder(root.right)


def preorder(root: Optional[TreeNode]):
  if not root:
    return
  print(root.val)
  preorder(root.left)
  preorder(root.right)


def postorder(root: Optional[TreeNode]):
  if not root:
    return
  postorder(root.left)
  postorder(root.right)
  print(root.val)
