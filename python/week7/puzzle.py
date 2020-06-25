"""
3square puzzle class

J. Knerr
Fall 2017
"""

class Puzzle(object):
  """puzzle class"""

  def __init__(self, filename):
    """constructor for puzzle objects, given filename"""

    self.board = ["   ","   ","   "]   # empty board for 3x3 puzzle
    # read in the puzzle from file    
    inf = open(filename, "r")
    # any variable that starts with self is an INSTANCE variable
    self.clues = []
    self.answers = []
    for line in inf:
      #ice:cold cube
      data = line.strip().split(":")
      self.answers.append(data[0])
      self.clues.append(data[1])
    inf.close()

  def display(self):
    """show board progress and clues"""
    self._display(self.board)

  def displayAnswers(self):
    """show answers and clues"""
    self._display(self.answers)

  # methods that start with _ are "private" (not meant to be used by
  # class user...just as helper functions in class)
  def _display(self,ans):
    """helper method...show ans and clues"""
    print("-"*30)
    for i in range(len(self.clues)):
       print(" %s|%s|%s  %d. %s" % (ans[i][0], ans[i][1], ans[i][2], i+1, self.clues[i]))
    print("\n")

  def setRow(self,rownum,word):
    """given word, add it to board at given row number"""
    self.board[rownum-1] = word

  def checkSolution(self):
    """return True if they have solved the puzzle"""
    for i in range(len(self.board)):
      if self.board[i] != self.answers[i]:
        return False
    # if we get here, puzzle is solved
    return True

def testcode():
  p = Puzzle("puzzle.txt")
  p.display()
  p2 = Puzzle("puzzle2.txt")
  p2.display()
  p2.setRow(2,"uno")
  assert(p2.checkSolution()==False)
  p2.display()
  p2.displayAnswers()
  p2.setRow(1,"out")
  p2.setRow(3,"too")
  assert(p2.checkSolution()==True)

if __name__ == "__main__":
  testcode()

