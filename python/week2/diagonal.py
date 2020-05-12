"""
diagonal fun with strings...

J. Knerr
Spring 2020
"""

def main():
    text = input("text: ")
    for i in range(len(text)-2):
        three = text[i:i+3]        # more slicing
        spaces = i * "   "
        print("%s%s" % (spaces,three))

main()
