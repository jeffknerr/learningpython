"""
  find all anagrams of given word, using recursion
"""
from random import *

###########################################################

def main():
  """ get a word, figure out and print the anagrams...  """

  wordfile = "/usr/share/dict/words"  # all english words
  wordfile = "words.txt"  # all english words
  english = readDictionary(wordfile)
  while True:
    word = input("  Enter word: ")
    if word == "":
      break
    word = word.lower()
    alist = anagrams(word)
#   print(alist)
    print("\n%d words to lookup..." % len(alist))
    displayAnagram(alist,english)

###########################################################

def binarySearch(x,L):
  """
  use binary search method to determine if x is in L.
  return True if it is, False if it is not...
  """

  low = 0
  high = len(L) - 1

  while True:
    if low > high:
      return False

    mid = (low + high)//2

    if x == L[mid]:
      return True
    elif x < L[mid]:
      high = mid - 1
    elif x > L[mid]:
      low = mid + 1

###########################################################

def displayAnagram(alist,english):
  """
  given a list of all possible permutations, print only
  the ones that are in the list of english words
  """

  uniqalist = []
  for word in alist:
    if word not in uniqalist:
      # if word in english:
      if binarySearch(word,english):
        uniqalist.append(word)
  print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
  for word in uniqalist:
    print(word)
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

###########################################################

def anagrams(s):
  """
  Zelle recursive anagrams function:
  returns a list of all anagrams of string s
  """
  if s == "":
      return [s]
  else:
      ans = []
      for w in anagrams(s[1:]):
          for pos in range(len(w)+1):
              ans.append(w[:pos]+s[0]+w[pos:])
      return ans

###########################################################

def readDictionary(fname):
  """
  given file name, open and read the words into a list.
  ignore blank lines and lines that start with a pound sign.
  return the lowercase words as a list.
  """
  words = []
  infile = open(fname, 'r')
  for line in infile:
    if (line[0] != '#') and (line[0] != '\n') and (line[0].islower()):
      word = line.strip()
      words.append(word.lower())
  return words

###########################################################

if __name__ == '__main__': main()
