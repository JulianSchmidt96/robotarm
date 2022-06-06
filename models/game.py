import numpy as np


class Game(Object):
    
    def __init__(self):
        
        """
        _description_
        set a 3x3 matrix filled with Nans as a start board.
        Two players will start to overwrite the 2s with 0 or 1 values.
        
        """
        self.board=np.full((3,3),np.nan)
        
  
    
    
    def get_value(coordinates):
        """_summary_

        Args:
            coordinates (list of integers): x, y coordinates

        Returns:
            value(str or np.nan): value at coordinates 
        """
        
        return board[coordinates[0],coordinates[1]]
    
    
        
    def set(self, coordinates, value):
        
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
        
        if not (value == 'A' or value =='B'):
            print('value is invalid')
            return False
        
        board[coordinates[0],coordinates[1]]=value
                        
            
        return True