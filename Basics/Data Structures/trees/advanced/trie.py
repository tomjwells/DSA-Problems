from typing import Self


class TrieNode:
  children: dict[str, Self]
  word: bool  # Mark the last character as the end of the word, to distinguish between "apple" and "a" for example

  def __init__(self):
    self.children = {}
    self.word = False


class Trie:
  root: TrieNode

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str):
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    curr.word = True

  def search(self, word: str):
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    # Means that search("a") returns False unless "a" is a word (even if "apple" is in the trie)
    return curr.word

  def startsWith(self, prefix: str):
    curr = self.root
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return True
