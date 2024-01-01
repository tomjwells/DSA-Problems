from typing import Any


class ListNode:
  def __init__(self, val: Any):
    self.val = val
    self.next = None


# Implementation for Singly Linked List


class LinkedList:
  head: ListNode
  next: ListNode
  tail: ListNode

  def __init__(self):
    # Init the list with a 'dummy' node which makes
    # removing a node from the beginning of list easier.
    self.head = ListNode(-1)
    self.tail = self.head

  def insertEnd(self, val: Any):
    self.tail.next = ListNode(val)
    self.tail = self.tail.next

  def remove(self, index: int):
    i = 0
    curr = self.head
    while i < index and curr:
      i += 1
      curr = curr.next

    # Remove the node ahead of curr
    if curr:
      curr.next = curr.next.next

  def print(self):
    curr = self.head.next
    while curr:
      print(curr.val, " -> ")
      curr = curr.next
    print()
