class Board:
  def __init__(self):
    self.board = [[0 for i in range(10)] for j in range(10)]

  def isValidMove(self, x, y):
    if x < 0 or x > 9 or y < 0 or y > 9:
      return False
    if self.board[x][y] == 0 or self.board[x][y] == 1 or self.board[x][y] == 2 or self.board[x][y] == 3 or self.board[x][y] == 4 or self.board[x][y] == 5:
      return True
    return False

  def getHiddenBoard(self):
    hiddenDict = {0:" " , 1:" " , 2:" " , 3:" " , 4:" " , 5:" ", 6:"O" , 7:"X"}
    hiddenBoard = "-----------------------------------------\n"
    for y in range(0, 10):
      hiddenBoard = hiddenBoard + "| "
      for x in range(0, 10):
        hiddenBoard = hiddenBoard + hiddenDict[self.board[x][y]] + "   "
      hiddenBoard = hiddenBoard + "|\n"
    hiddenBoard = hiddenBoard + "-----------------------------------------"
    return hiddenBoard    
