"""
fun with strings...

J. Knerr
Spring 2020
"""

def main():
    text = input("text: ")
    half = len(text)//2       # integer math
    firsthalf = text[:half]   # use slicing
    secondhalf = text[half:]  # use slicing
    for ch in firsthalf:
        print("%s|" % (ch))
    for ch in secondhalf:
        print(" |%s" % (ch))

main()
