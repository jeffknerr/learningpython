"""
split given text into 5-letter blocks

J. Knerr
Spring 2020
"""

def main():
    text = input("input text: ")
    # klunky, but this is all we know so far...we'll learn better
    # ways to do this later
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    counter = 0   # count letters per word
    perline = 0   # count words per line
    for ch in text:
        if ch in letters:
            counter += 1
            output += ch
            if counter == 5:
                output += " "   # add space between words
                counter = 0
                perline += 1
            if perline == 5:
                output += "\n"  # add newline between lines
                perline = 0
    print(output)

main()
