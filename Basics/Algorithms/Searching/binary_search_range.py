def binarySearch(low: int, high: int):
  """
  Binary search on some range of values
  """

  while low <= high:
    mid = (low + high) // 2

    if isCorrect(mid) > 0:
      high = mid - 1
    elif isCorrect(mid) < 0:
      low = mid + 1
    else:
      return -1
    return mid


def isCorrect(n: int):
  """
  Return 1 if n is too big, -1 if too small, 0 if correct
  """
  if n > 10:
    return 1
  elif n < 10:
    return -1
  else:
    return 0
