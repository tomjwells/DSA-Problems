# write a function is_anagram (wl, w2)
#
# two words are anagrams if you can rearrange the letters and they are the same

from collections import Counter

import pytest

# "sorted" solution


def is_anagram_sorted(w1: str, w2: str) -> bool:
  return sorted(w1) == sorted(w2)


# runtime: n*log(n)
#  - sorting is n*log(n)
#  - list comparison is O(n)

# A better runtime is achievable with Counter (O(n))


def is_anagram(w1: str, w2: str) -> bool:
  return Counter(w1) == Counter(w2)


@pytest.mark.parametrize(
    ("w1", "w2", "expected"),
    (
        ("", "", True),
        ("", "a", False),
        ("a" "b", False),
        ("bleat", "table", True),
        ("foo", "of", False),
        ("foo", "ffo", False),
    ),
)
def test_is_anagram(w1: str, w2: str, expected: bool):
  assert is_anagram(w1, w2) is expected
