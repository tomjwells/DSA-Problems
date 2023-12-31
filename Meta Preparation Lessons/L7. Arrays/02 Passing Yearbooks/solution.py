from typing import List

# Add any extra import statements you may need here


# Add any helper functions you may need here


def findSignatureCounts(arr: List[int]):
  # Write your code here
  n = len(arr)
  finished_array = [i + 1 for i in range(n)]
  sigs = [1] * n
  iterations = 0
  while True:
    iterations += 1
    print(arr)
    temp_array = arr.copy()
    if arr == finished_array:
      break
    else:
      for i in range(n):
        if i == 0:
          temp_val = arr[n - 1]
        else:
          temp_val = arr[i - 1]
        if temp_val == i:
          pass
        else:
          sigs[i] += 1
          if i == 0:
            arr[n - 1] = temp_array[i]
          else:
            arr[i - 1] = temp_array[i]
  return sigs


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
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
