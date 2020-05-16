"""
simple example of rolling dice

J. Knerr
Spring 2020
"""

import random

def main():
    pig = ["leftside","rightside","razorback","trotter","snouter","jowler","bacon"]
    rolls = getInt("How many rolls? ")
    for i in range(rolls):
        r1 = random.choice(pig)
        r2 = random.choice(pig)
        if r1=="bacon" or r2=="bacon":
            score = 0
        elif (r1=="leftside" and r2=="rightside") or r1=="rightside" and r2=="leftside":
            score = 0
        elif (r1=="leftside" and r2=="leftside") or r1=="rightside" and r2=="rightside":
            score = 1
        elif r1 == r2:
            score = 4*scoreOnePig(r1)
        else:
            score = scoreOnePig(r1) + scoreOnePig(r2)
        print("roll %2d: %10s, %10s -- score: %2d" % (i+1,r1,r2,score))


def scoreOnePig(roll):
    """return score for one roll of pig dice"""
    if roll == "leftside" or roll == "rightside":
        return 1
    elif roll == "razorback":
        return 5
    elif roll == "trotter":
        return 5
    elif roll == "snouter":
        return 10
    elif roll == "jowler":
        return 15
    else:
        return None

def getInt(prompt):
    """get int without crashing..."""
    while True:
        n = input(prompt)
        try:
            n = int(n)
            return n
        except ValueError:
            print("please enter an integer...")

main()
