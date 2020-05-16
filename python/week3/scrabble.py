"""
simple scrabble score -- show use of parallel lists

J. Knerr
Spring 2020
"""

def main():
    letters = list("abcdefghijklmnopqrstuvwxyz")
    scores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

    word = input("scabble word: ")
    total = 0
    for ch in word:
        for i in range(len(letters)):
            if letters[i] == ch:
                points = scores[i]
                print("letter: %s (index: %2d), score for letter = %2d" % (ch,i,points))
                total += points
    print("\ntotal score for %s: %d" % (word,total))

main()
