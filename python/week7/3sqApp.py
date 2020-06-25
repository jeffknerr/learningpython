"""
3x3 puzzle game using Puzzle class

J. Knerr
Fall 2017
"""

from puzzle import *

def main():
  print("\n --- Welcome to 3square! --- \n")
  p = Puzzle("puzzle.txt")

  done = False
  while not done:
     p.display()
     choice = getChoice()
     if choice == 'q':
        done = True
        print("\nquitter! :(\n")
     else:
        row = int(choice)
        word = getWord(row)
        p.setRow(row,word)
        done = p.checkSolution()
        if done:
           print("\nYou solved it!!\n")
  p.displayAnswers()

# -------------------------------- #

def getChoice():
  """get and return user's choice"""
  valids = list("123")
  while True:
    uc = input("q123> ")
    if uc == "q":
      return uc
    elif uc in valids:
      return int(uc)
    else:
      print("\nPlease enter q, 1, 2, or 3...\n")

def getWord(row):
  """given row (1,2,3), get user answer"""
  while True:
    word = input("%d: " % row).lower()
    if len(word) == 3 and word.isalpha():
      return word
    else:
      print("Please enter a 3-letter word...")

# -------------------------------- #

main()
