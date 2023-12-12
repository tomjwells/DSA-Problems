# Iterative version
# Time: O(log(n)) | Space: O(1)
def binary_search(array, target):
  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

# Recursive version
# Time: O(log(n)) | Space: O(log(n))
def binary_search_recursive(array, target):
  return binary_search_helper(array, target, 0, len(array) - 1)

def binary_search_helper(array, target, low, high):
  if low > high:
    return -1
  mid = (low + high) // 2
  if array[mid] == target:
    return mid
  elif array[mid] < target:
    return binary_search_helper(array, target, mid + 1, high)
  else:
    return binary_search_helper(array, target, low, mid - 1)
  

# Examples:
print(binary_search([1, 2, 3, 4, 5], 5)) # 4
print(binary_search_recursive([1, 2, 3, 4, 5], 5)) # 4
print(binary_search([1, 2, 3, 4, 5], 1)) # 0
print(binary_search_recursive([1, 2, 3, 4, 5], 1)) # 0
print(binary_search([1, 2, 3, 4, 5], 3)) # 2
print(binary_search_recursive([1, 2, 3, 4, 5], 3)) # 2
