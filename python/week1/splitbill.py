"""
Splitting the bill program

J. Knerr
Spring 2020
"""

def main():
    amt = float(input("  bill amount: "))
    pct = float(input("  percent tip: "))
    num =   int(input("num of people: "))

    tip = amt*(pct/100)
    total = amt + tip
    cpp = total/num       # cost per person

    print("-=-"*10)
    print("     tip = $%6.2f" % (tip))
    print("   total = $%6.2f" % (total))
    print("cost per = $%6.2f" % (cpp))

main()
