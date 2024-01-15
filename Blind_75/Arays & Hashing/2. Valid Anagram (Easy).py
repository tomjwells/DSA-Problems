class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Initialize dicts
    s_characters: dict[str, int] = {}
    t_characters: dict[str, int] = {}

    for char in s:
      if char in s_characters:
        s_characters[char] = s_characters.get(char, 0) + 1

    for char in t:
      if char in t_characters:
        t_characters[char] = t_characters.get(char, 0) + 1

    for char in alphabet:
      if s_characters.get(char) == t_characters.get(char):
        pass
      else:
        return False

    return True
