from typing import Any, Optional, Self


class ListNode:
  val: int
  next: Optional[Self]

  def __init__(self, val: Any):
    self.val = val
    self.next = None


# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(head: ListNode):
  slow, fast = head, head
  while fast and fast.next and slow.next:
    slow = slow.next
    fast = fast.next.next
  return slow


# Determine if the linked list contains a cycle.
# Time: O(n), Space: O(1)
def hasCycle(head: ListNode):
  slow, fast = head, head
  while fast and fast.next and slow.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False


# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head: ListNode):
  slow, fast = head, head
  while fast and fast.next and slow.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break

  if not fast or not fast.next:
    return None

  slow2 = head
  while slow != slow2 and slow.next and slow2.next:
    slow = slow.next
    slow2 = slow2.next
  return slow
