"""
ask for number of terms, calculate series to that many terms:

    1 + 1/(2**2) + 1/(3**2) + ...

if enough terms, should converge to 1.64493

J. Knerr
Spring 2020
"""

import math

def main():
    n = int(input("number of terms: "))
    result = 0
    for i in range(1,n+1):
        term = 1/(i**2)
        result = result + term
        print("%4d. %7.5f" % (i, result))
    picalc = math.sqrt(6*result)
    print("\nFor %d terms I calculate pi = %7.5f" % (n, picalc))

main()
