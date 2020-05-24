"""
three-card monte game

J. Knerr
Fall 2019
"""

from random import choice

def main():
  done = False
  positions = ["A","B","C"]
  round = 1
  while not done:
    position = choice(positions)
    print(">>> Round %d..." % (round))
    answer = getPick()
    if answer == position:
      print("Correct!")
      done = True
    else:
      print("Nope....it was in position %s!" % (position))
      print("="*30)
      round = round + 1

def getPick():
  """get user's pick: A, B, or C"""
  while True:
    pick = input("Where is the Queen of Hearts? [A,B,C]: ")
    if pick == "A" or pick == "a":
      return "A"
    elif pick == "B" or pick == "b":
      return "B"
    elif pick == "C" or pick == "c":
      return "C"
    else:
      print("Please enter A, B, or C!!")

main()
