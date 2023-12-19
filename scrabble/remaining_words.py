#! /usr/bin/python3

"""
show how many remaining 5-letter words there are, based on
a few facts (e.g., ends in 'e', contains an 'r', does
not contain an 'i', etc).

J. Knerr
April 2022
"""

# add starts with
# add multiple-letter adds to contains, does not contain
# reuse functions?

instructions = """

use menu options to enter letters in word.
hit <Enter> at menu prompt to see remaining words.
"""

def main():
    words = readwords()
    done = False
    rules = {}
    print(instructions)
    while not done:
        print("-"*30)
        print("words remaining: %d" % (len(words)))
        opt = menu()
        if len(opt) == 0:
            done = True
        elif opt == "e":
            endswith(words, rules)
        elif opt == "s":
            startsWith(words, rules)
        elif opt == "c":
            contains(words, rules)
        elif opt == "d":
            doesnotcontain(words, rules)
    print("Here are your remaining words...")
    for word in words:
        print(word)
    print("For these rules...")
    for key in rules:
        print("%s %s" % (key, rules[key]))

def startsWith(words, rules):
    """add startsWith rule, take out all words that don't match"""
    letter = input('starts with letter: ').lower()
    rules['startswith'] = letter
    # work backward through list so we don't skip items as we pop them
    for i in range(len(words)-1, -1, -1):
        if not words[i].startswith(letter):
            words.pop(i)

def endswith(words, rules):
    """add endswith rule, take out all words that don't match"""
    letter = input('ends with letter: ').lower()
    rules['endswith'] = letter
    # work backward through list so we don't skip items as we pop them
    for i in range(len(words)-1, -1, -1):
        if not words[i].endswith(letter):
            words.pop(i)


def contains(words, rules):
    """add contains rule, take out all words that don't match"""
    letter = input('contains letter: ').lower()
    if 'contains' in rules:
        rules['contains'].append(letter)
    else:
        rules['contains'] = [letter]
    for i in range(len(words)-1, -1, -1):
        if letter not in words[i]:
            words.pop(i)


def doesnotcontain(words, rules):
    """add does not contain rule, take out all words that don't match"""
    letter = input('does not contain letter: ').lower()
    if 'doesnotcontain' in rules:
        rules['doesnotcontain'].append(letter)
    else:
        rules['doesnotcontain'] = [letter]
    for i in range(len(words)-1, -1, -1):
        if letter in words[i]:
            words.pop(i)


def menu():
    """present menu to user, return option chosen"""
    options = ["", "e", "s", "c", "d"]
    prompt = "/".join(options) + ": "
    while True:
        opt = input(prompt).strip().lower()
        if opt == "?":
            print("""
            Enter for done
            e:ends with
            s:starts with
            c:contains
            d:does not contain""")
        if opt in options:
            return opt
        else:
            print("Please choose an option from the list. Type ? for help")


def readwords():
    """read in all 5 letter words"""
    inf = open("/usr/share/dict/words", "r")
    words = []
    for line in inf:
        word = line.strip()
        if len(word) == 5 and word.islower() and word.isalpha():
            words.append(word)
    inf.close()
    return words


main()
