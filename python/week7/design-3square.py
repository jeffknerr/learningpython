"""
3x3 puzzle game

J. Knerr
Fall 2017
"""

def main():
  uanswers = ["   ","   ","   "]  # user's answers so far
  clues,answers = readFile("puzzle.txt")
  done = False
  while not done:
    display(clues, uanswers)
    choice = getChoice()
    if choice == 'q':
      done = True
      display(clues, answers)
    else:
      update(uanswers,clues,answers,choice)
      done = check(uanswers,answers)
      if done:
        print("\nYou solved it!!\n")

# -------------------------------- #

def readFile(filename):
  """read in puzzle from file, return as list of clues and answers"""
  clues = ["q1","q2","q3"]
  answers = ["xxx","yyy","zzz"]
  return clues, answers

def getChoice():
  """get and return user's choice"""
  uc = input("> ")
  return uc

def display(clues, answers):
  """display clues and answers in pretty format"""
  print(clues)
  print(answers)

def update(uanswers,clues,answers,choice):
  """given choice (1,2,3), get user answer and update board"""
  num = int(choice)
  word = input("%d: " % num)
  uanswers[0] = word

def check(uanswers,answers):
  """check if they have solved the puzzle"""
  return False

# -------------------------------- #

main()
