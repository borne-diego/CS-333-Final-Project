import unittest
from board import Board
from game import Game
from player import Player
import random
import main

class boardTests(unittest.TestCase):
  def setUp(self):
    self.board = Board()

  def testConstructor(self):
    self.assertEqual(self.board.board, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testisValidMoveOutOfBounds(self):
    self.assertTrue(self.board.isValidMove(10, 9))

  def testisValidMoveInvalidBoardValue(self):
    self.board.board[0][0] = 7
    self.assertFalse(self.board.isValidMove(0, 0))

  def testisValidMoveValidPosAndValue(self):
    self.assertTrue(self.board.isValidMove(1, 1))

  def testgetHiddenBoard(self):
    self.assertEqual(self.board.getHiddenBoard(),"-----------------------------------------\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n|                                         |\n-----------------------------------------")

class playerTests(unittest.TestCase):
  def setUp(self):
    self.player = Player()

  def testConstructor(self):
    self.assertEqual(self.player.ships, [5, 4, 3, 3, 2])

  def testplayerLostFalse(self):
    self.assertFalse(self.player.playerLost())

  def testplayerLostTrue(self):
    self.player.ships = [0, 0, 0, 0, 0]
    self.assertTrue(self.player.playerLost())

class gameTests(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  def testConstructorPlayer(self):
    self.assertEqual(self.game.player1.ships, [5, 4, 3, 3, 2])

  def testConstructorBoard(self):
    self.assertEqual(self.game.board1.board,[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testgameSetupBoard1(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    self.assertEqual(self.game.board1.board,[[1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testgameSetupBoard2(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    self.assertEqual(self.game.board2.board,[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 0, 0, 0, 0], [0, 0, 0, 0, 4, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testgameMovePlayer1ValidMiss(self):
    self.game.gameMove(0, 0, 1)
    self.assertEqual(self.game.board2.board,[[6, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testgameMovePlayer1ValidHit(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    self.game.gameMove(5, 5, 1)
    self.assertEqual(self.game.board2.board, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 7, 0, 0, 0, 0], [0, 0, 0, 0, 4, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testgameMovePlayer1InvalidMoveExceptionBounds(self):
    with self.assertRaises(Exception) as context:
      self.game.gameMove(100, 10, 1)
    self.assertEqual(str(context.exception), "invalid move")

  def testgameMovePlayer1InvalidMoveExceptionInvalidBoardValue(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    self.game.gameMove(5, 5, 1)
    with self.assertRaises(Exception) as context:
      self.game.gameMove(5, 5, 1)
    self.assertEqual(str(context.exception), "invalid move")

  def testgameMovePlayer1PlayerShipDecrement(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    self.game.gameMove(5, 5, 1)
    self.assertEqual(self.game.player2.ships[4], 1)

  def testgameMovePlayer2ValidMove(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    self.game.gameMove(0, 0, 2)
    self.assertEqual(self.game.board1.board, [[7, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testcheckWinPlayer1Win(self):
    self.game.player1.ships = [0, 0, 0, 0, 0]
    self.assertEqual(self.game.checkWin(), 1)

  def testcheckWinPlayer2Win(self):
    self.game.player2.ships = [0, 0, 0, 0, 0]
    self.assertEqual(self.game.checkWin(), 2)

  def testcheckWinNoWinner(self):
    self.assertEqual(self.game.checkWin(), -1)

  def testcomputerMoveSeededAllMisses(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    random.seed(10)
    self.game.computerMove()
    self.assertEqual(self.game.board1.board, [[1, 2, 3, 4, 5, 0, 0, 0, 0, 6], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 6, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

  def testcomputerMoveSeededHit(self):
    self.game.gameSetup([0, 0, 0, 1, 0, 2, 0, 3, 0, 4], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    random.seed(1231)
    self.game.computerMove()
    self.assertEqual(self.game.board1.board, [[1, 2, 3, 4, 7, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 6, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 6, 0, 0, 0]])

if __name__ == "__main__":
  unittest.main()
