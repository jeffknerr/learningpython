"""
Walks plus Hits per Innings Pitched

J. Knerr
Spring 2020
"""

def main():
    walks   = getInt("  walks: ")
    hits    = getInt("   hits: ")
    innings = getInt("innings: ")
    whip = (walks+hits)/innings

    if whip <= 1.00:
        rating = "excellent"
    elif whip <= 1.10:
        rating = "great"
    elif whip <= 1.25:
        rating = "above average"
    elif whip <= 1.32:
        rating = "average"
    elif whip <= 1.40:
        rating = "below average"
    elif whip <= 1.50:
        rating = "poor"
    else:
        rating = "awful"

    print("\nWHIP = %.2f (%s)" % (whip, rating))


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
