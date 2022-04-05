
# make a scramble puzzle

# fix to only allow words possible with scrabble letters?
# e.g., no words with 2 z's??

# got 7-letter wordlist from 
# https://www.wordgamedictionary.com/word-lists/

# todo:
#  - add a few 6-letter words with high letter values
#  - make the 6-letter word double or triple score?
#  - or make the highest letter of one word a double-letter score
#  - add graphics to display tiles

import random
import matplotlib.pyplot as plt

letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 
                'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 
                'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 
                'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

#fn = "words.txt"
fn = "/usr/share/dict/words"
words = []
inf = open(fn,"r")
for line in inf:
    word = line.strip()
    if word.isalpha() and word.islower() and len(word) == 7:
        words.append(word)
inf.close()

def plot(words):
    fig = plt.figure(figsize=(8, 10))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    word = words[1]
    y = 0.9
    for word in words:
      x = 0.05
      for i in range(len(word)):
        ch = word[i].upper()
        plt.text(x, y, ch, size=30, rotation=0., ha="center", va="center", 
           fontfamily='monospace',
           bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),))
        x = x + 0.1
      y = y - 0.2
    plt.show()
    #plt.savefig(fname="plot.jpg")


def spaced(word):
    new = "| "
    for ch in word:
        new += ch + " | "
    return new

def getscore(word):
    score = 0
    for ch in word:
        score += letter_value[ch]
    return score

def pprint(num, word):
    """pretty-print the word"""
    print()
    print("        "+("--- "*7))
    print("    %d: %s" % (num, spaced(word).upper()))
    print("        "+("--- "*7))
    print()

line = "="*40
print("\n\n"+line)
N = 5
answers = []
total = 0
choosen = []
for i in range(N):
    word = random.choice(words)
    score = getscore(word)
    total = total + 50 + score
    answers.append(word)
    listword = list(word)
    random.shuffle(listword)
    scrambled = "".join(listword)
    choosen.append(scrambled)
    pprint(i+1, scrambled)
print("\n"+ line + "\n")
print(" total score = %d" % (total))
print("\n"+ line + "\n")

ofile = open("answers.txt","w")
for i in range(len(answers)):
    ofile.write("%d. %s\n" % (i+1, answers[i].upper()))
ofile.close()

plot(choosen)
