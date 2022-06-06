import numpy as np


class Game():
    
    def __init__(self):
        
        """
        _description_
        set a 3x3 matrix filled with Nans as a start board.
        Two players will start to overwrite the 2s with 0 or 1 values.
        
        creare variable to save current Player name
        """
        self.board = np.full((3,3),np.nan)
        self.turn = None
    
    def toss(self):
        
        """Function to simulate a toss and decide which player goes first

        Args:

        Returns:
        Returns 1 if player assigned mark 1 has won, or 0 if his opponent won

        """
        self.turn=np.random.randint(0,2,size=1)
        if self.turn.mean() == 0:
            self.turn = 0
        elif self.turn.mean() == 1:
            self.turn = 1
        return self.turn
    
    def switch_turn(self):
        turn = self.turn
        if turn == 0:
            self.turn = 1
        if turn == 1:
            self.turn = 0
        return True
        
            
        
        
        
        
  
    
    
    def get_value(coordinates):
        """_summary_

        Args:
            coordinates (list of integers): x, y coordinates

        Returns:
            value(str or np.nan): value at coordinates 
        """
        
        return board[coordinates[0],coordinates[1]]
    
    
        
    def set(self, coordinates):
        
        """
        _summary_
            Args:
                coordinates (list of integers): col, row coordinates where value is set
                value ( int) : 0 or 1 ( depending on player)
            Returns:
                bool:   True if move was valid
                        False if move was not valid
        
        
        _description_
            Check if coordinates and value are valid
            Replace value at the given coordinates with the given value and return True/False depending if move was valid
        """
        
        if not (coordinates[0] >= 0 and coordinates[0] <= 2):
            print('x coordinate is wrong')
            return False
        
        if not (coordinates[1] >= 0 and coordinates[1] <= 2):
            print('y coordinate is wrong')
            return False
        
        if not (self.turn == 1 or self.turn ==0):
            print('value is invalid')
            return False
        
        
        if not np.isnan(self.board[coordinates[0],coordinates[1]]):
            print('Field allready taken')
            return False
        
        self.board[coordinates[0],coordinates[1]] = self.turn
        self.switch_turn()
            
        return True
    