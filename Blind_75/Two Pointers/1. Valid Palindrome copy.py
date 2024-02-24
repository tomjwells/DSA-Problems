class Solution:
  def isPalindrome(self, s: str) -> bool:
    new_s = s.lower()
    final_s = "".join(char for char in new_s if char.isalnum())

    # Init pointers
    is_even = len(final_s) % 2 == 0
    if is_even:
      l = (len(final_s) // 2) - 1
      r = len(final_s) // 2
    else:
      l = r = len(final_s) // 2

    # Iterate
    if len(final_s) == 0:
      return True
    else:
      while True:
        if l > -1 and r < len(final_s) and final_s[l] == final_s[r]:
          if l == 0:
            return True
          else:
            l -= 1
            r += 1
        else:
          return False


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
