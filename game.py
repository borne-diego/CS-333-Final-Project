from board import Board
from player import Player
import random

class Game:
  def __init__(self):
    self.player1 = Player()
    self.player2 = Player()
    self.board1 = Board()
    self.board2 = Board()

  def gameSetup(self, p1Ships, p2Ships):
    for x in range(0, 5):
      self.board1.board[p1Ships[0]+x][p1Ships[1]] = 1
    for x in range(0, 4):
      self.board1.board[p1Ships[2]+x][p1Ships[3]] = 2
    for x in range(0, 3):
      self.board1.board[p1Ships[4]+x][p1Ships[5]] = 3
    for x in range(0, 3):
      self.board1.board[p1Ships[6]+x][p1Ships[7]] = 4
    for x in range(0, 2):
      self.board1.board[p1Ships[8]+x][p1Ships[9]] = 5

    for x in range(0, 5):
      self.board2.board[p2Ships[0]+x][p2Ships[1]] = 1
    for x in range(0, 4):
      self.board2.board[p2Ships[2]+x][p2Ships[3]] = 2
    for x in range(0, 3):
      self.board2.board[p2Ships[4]+x][p2Ships[5]] = 3
    for x in range(0, 3):
      self.board2.board[p2Ships[6]+x][p2Ships[7]] = 4
    for x in range(0, 2):
      self.board2.board[p2Ships[8]+x][p2Ships[9]] = 5

  def gameMove(self, x, y, player):
    enemy = Player()
    enemyBoard = Board()
    if player == 1:
      enemy = self.player2
      enemyBoard = self.board2
    else:
      enemy = self.player1
      enemyBoard = self.board1

    if enemyBoard.isValidMove(x, y):
      if enemyBoard.board[x][y] == 0:
        enemyBoard.board[x][y] = 6
      else:
        enemy.ships[enemyBoard.board[x][y]-1] = enemy.ships[enemyBoard.board[x][y]-1] - 1
        enemyBoard.board[x][y] = 7
    else:
      raise Exception("invalid move")

  def checkWin(self):
    if(self.player1.playerLost()):
        return 1
    elif(self.player2.playerLost()):
      return 2
    return -1

  def computerMove(self):
    for x in range(0, 3):
      y = random.randint(0, 9)
      x = random.randint(0, 9)
      tries = 0;
      while(not self.board1.isValidMove(x, y)):
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        tries += 1
        if(tries > 100):
          return
      self.gameMove(x, y, 2)