"""
roll until we get a yahtzee (5 of a kind)

J. Knerr
Spring 2020
"""

import random

def main():
    tries = 0
    done = False
    while not done:
        roll = rolldice(5)
        tries += 1
        print(roll)
        if roll[0]==roll[1]==roll[2]==roll[3]==roll[4]:
            done = True
    print("Yahtzee! (took %d tries)" % (tries))

def rolldice(n):
    """roll n 6-sided dice, return as a list"""
    results = []
    for i in range(n):
        die = random.randrange(1,7)
        results.append(die)
    return results

main()
