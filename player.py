class Player:
  def __init__(self):
    
    self.ships = [5, 4, 3, 3, 2]

  def playerLost(self):
    return (sum(self.ships) == 0)