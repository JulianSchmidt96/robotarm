import numpy as np

class GameManager():
    
    def __init__(self, game):
        
        """
        
        _summary_
            Args:
                board (object): from Game class
                player (string): 0 or 1
                
        """
    
        self.game = game
        
     
        
    
    def get_board_state(self):
        
        """
        
        -_summary_
            Args:
                board (object): from Game class
            Returns:
                "Won" if the game has been won, "Drawn" if the 
                game has been drawn, or "In Progress", if the game is still in progress
       
        _description_
                Function to check the current status of the game, 
                whether the game has been won, drawn or is in progress

        """
        board = self.game.board
        print(board)
        print(' ')
        print(f' its {self.game.turn} turn')
        #check for a win along rows
        for i in range(board.shape[0]):
            if np.nan not in board[i,:] and len(set(board[i,:]))==1:
                return "Won"
        #check for a win along columns
        for j in range(board.shape[1]):
            if np.nan not in board[:,j] and len(set(board[:,j]))==1:
                return "Won"
        # check for a win along diagonals
        if np.nan not in np.diag(board) and len(set(np.diag(board)))==1:
            return "Won"
        if np.nan not in np.diag(np.fliplr(board)) and len(set(np.diag(np.fliplr(board))))==1:
            return "Won"
        # check for a Draw
        if not np.isnan(board).any():
            return "Drawn"
        else:
            return "In Progress"
        
    
    def legal_moves_generator(self):
        
        """
    
        _summary_

            Args:
                board (object): from Game class
                turn_Monitor (object): from TurnMonitor class -> two see which Players turn it is

            Returns:
                legal_moves_dict: A dictionary of a list of possible next coordinate-resulting board state pairs
                The resulting board state is flattened to 1 d array
        
        _description_
                Function that returns the set of all possible legal moves and resulting board states, 
                for a given input board state and player



        """
        board = self.game.board
        turn = self.game.turn
        
        current_board_state = board
        legal_moves_dict={}
        for i in range(current_board_state.shape[0]):
            for j in range(current_board_state.shape[1]):
                if current_board_state[i,j] == np.nan:
                    
                    board_state_copy=current_board_state.copy()
                    board_state_copy[i,j] = turn
                    legal_moves_dict[(i,j)] = board_state_copy
                    
        return legal_moves_dict
    
    
    
    
    def set(self, coordinates):
        self.game.set(coordinates)
        