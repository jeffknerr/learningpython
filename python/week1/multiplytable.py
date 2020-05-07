"""
print out a multiplication table

J. Knerr
Spring 2020
"""

def main():
    factor = int(input("\nFactor? "))
    print("%s | %s" % ("n", str(factor) + "*n"))
    print("-"*7)
    for i in range(1,10):
        print("%d | %3d" % (i, i*factor))

main()
