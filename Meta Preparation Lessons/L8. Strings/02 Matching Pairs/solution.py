# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s: str, t: str):
  count = 0
  perfect_swapped = False
  imperfect_swap_is_possible = False
  potential_swaps = {}

  # There are three kinds of swaps:
  #  - Perfect swaps : ab, ba -> ab, ab (count += 2)
  #  - Imperfect swaps: ab, za -> ab, az (count += 1)
  #  - Destructive swaps: ab, ab -> ab, ba (count -= 2)
  # To maximize the count, we must do a perfect swap if possible

  for i in range(len(s)):
    if s[i] == t[i]:
      count += 1
    else:
      # s[i] != t[i]
      if not perfect_swapped:
        if s[i] in potential_swaps:
          # Do a swap
          if potential_swaps[s[i]] == t[i]:
            perfect_swapped = True
            count += 2
          else:
            imperfect_swap_is_possible = True
        else:
          # Add to dict, save it for later
          potential_swaps[t[i]] = s[i]
      else:
        pass

  if not perfect_swapped:
    # We must do a swap
    # Ideal is to do an imperfect swap. If that is not possible, do a destructive swap
    if imperfect_swap_is_possible:
      count += 1
    else:
      # Destructive swap
      count -= 2

  return count


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printInteger(n: int):
  print("[", n, "]", sep="", end="")


test_case_number = 1


def check(expected: int, output: int):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = "\u2713"
  wrongTick = "\u2717"
  if result:
    print(rightTick, "Test #", test_case_number, sep="")
  else:
    print(wrongTick, "Test #", test_case_number,
          ": Expected ", sep="", end="")
    printInteger(expected)
    print(" Your output: ", end="")
    printInteger(output)
    print()
  test_case_number += 1


if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
