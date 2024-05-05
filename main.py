from game import Game
import os


def main():
  game = Game()
  game.gameSetup([0, 0, 2, 3, 4, 4, 0, 8, 5, 7], [0, 0, 2, 3, 4, 4, 0, 8, 5, 7])
  print("Welcome to Battleships!\nHits are represented by X, misses by O, unknown locations by ?.\nCarriers are 5 spaces long, battleships are 4, cruisers are 3, submarines are 3, destroyers are 2.\nYou play against a computer which moves three times per your one move. Good luck\n\n")
  result = -1
  while(result == -1):
    print("Enter coordinates to attack! (1-10)")
    x, y = (input("x: "), input("y: "))
    os.system("clear")
    try:
      game.gameMove(int(x)-1, int(y)-1, 1)
    except:
      print("Invalid coordinates!")
    game.computerMove()
    print("Your Board:\n" + game.board1.getHiddenBoard())
    print("Computer Board:\n" + game.board2.getHiddenBoard())
    result = game.checkWin()
  if(result == 1):
    print("You Lost!")
  else:
    print("You Win!")

if __name__ == "__main__":
  main()
