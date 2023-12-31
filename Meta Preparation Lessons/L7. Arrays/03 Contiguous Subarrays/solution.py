from typing import List

# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(arr: List[int]) -> List[int]:
  # Write your code here
  output: List[int] = []
  for i, _x in enumerate(arr):
    count_left = 0
    count_right = 0
    # Count rightward contiguous subarrays
    j = i
    while True:
      j += 1
      if j >= len(arr):
        break
      else:
        if arr[j] > arr[i]:
          break
        else:
          count_right += 1
    # Count leftward contiguous subarrays
    j = i
    while True:
      j -= 1
      if j < 0:
        break
      else:
        if arr[j] > arr[i]:
          break
        else:
          count_left += 1
    output.append(1 + count_left + count_right)
  return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printInteger(n: int):
  print("[", n, "]", sep="", end="")


def printIntegerList(array: List[int]):
  size = len(array)
  print("[", end="")
  for i in range(size):
    if i != 0:
      print(", ", end="")
    print(array[i], end="")
  print("]", end="")


test_case_number = 1


def check(expected: List[int], output: List[int]):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= output[i] == expected[i]
  rightTick = "\u2713"
  wrongTick = "\u2717"
  if result:
    print(rightTick, "Test #", test_case_number, sep="")
  else:
    print(wrongTick, "Test #", test_case_number,
          ": Expected ", sep="", end="")
    printIntegerList(expected)
    print(" Your output: ", end="")
    printIntegerList(output)
    print()
  test_case_number += 1


if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)

  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
