"""
simple blackjack simulator

J. Knerr
Fall 2019
"""

from random import randrange

def main():
  limit = 15
  games = 10
  over = 0
  for g in range(games):
    points = oneHand(limit)
    output = "Game %d Final total = %2d" % (g+1,points)
    if points > 21:
      output += " :("
      over += 1
    elif points == 21:
      output += " :)"
    print(output)
    print("= "*20)
  print("For %d games and limit=%d: %d went over." % (games, limit, over))

def oneHand(limit):
  """play one hand of blackjack, return points"""
  points = 0
  card1 = randrange(1,11)
  points += card1
  card2 = randrange(1,11)
  points += card2
  print("Card1: %2d, Card2: %2d -- total = %2d" % (card1,card2,points))
  while points <= limit:
    card = randrange(1,11)
    points += card
    print("Next Card: %2d           total = %2d" % (card,points))
  return points

main()
