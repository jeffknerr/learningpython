"""
3x3 puzzle game

J. Knerr
Fall 2017
"""

def main():
  print("\n --- Welcome to 3square! --- \n")

  uanswers = ["   ","   ","   "]  # user's answers so far
  clues,answers = readFile("puzzle.txt")
  display(clues, uanswers)

  done = False
  while not done:
    choice = getChoice()
    if choice == 'q':
      done = True
      display(clues, answers)
    else:
      update(uanswers,clues,answers,choice)
      done = check(uanswers,answers)
      if done:
        print("\nYou solved it!!\n")
      display(clues, uanswers)

# -------------------------------- #

def readFile(filename):
  """read in puzzle from file, return as list of clues and answers"""
  inf = open(filename, "r")
  clues = []
  answers = []
  for line in inf:
    #ice:cold cube
    data = line.strip().split(":")
    answers.append(data[0])
    clues.append(data[1])
  inf.close()
  return clues, answers

def getChoice():
  """get and return user's choice"""
  valids = list("123")
  while True:
    uc = input("q123> ")
    if uc == "q":
      return uc
    elif uc in valids:
      return int(uc)
    else:
      print("\nPlease enter q, 1, 2, or 3...\n")

def display(clues, answers):
  """display clues and answers in pretty format"""
  print("-"*30)
  for i in range(len(clues)):
    print(" %s|%s|%s  %d. %s" % (answers[i][0], answers[i][1], answers[i][2], i+1, clues[i]))
  print("\n")

def update(uanswers,clues,answers,choice):
  """given choice (1,2,3), get user answer and update board"""
  while True:
    word = input("%d: " % choice)
    if len(word) == 3 and word.isalpha():
      uanswers[choice-1] = word.upper()
      return
    else:
      print("Please enter a 3-letter word...")

def check(uanswers,answers):
  """check if they have solved the puzzle"""
  for i in range(len(answers)):
    if uanswers[i].lower() != answers[i].lower():
      return False
  # if we get here, all good
  return True

# -------------------------------- #

main()
