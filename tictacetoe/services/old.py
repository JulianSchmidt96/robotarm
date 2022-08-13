import numpy as np
import pandas as pd 


    


class GameManager(object):
    
    def __init__(self):
        self.board=np.full((3,3),2)
        
    def start_new_game(self):
        pass

    def toss(self):
        
        """Function to simulate a toss and decide which player goes first

        Args:

        Returns:
        Returns 1 if player assigned mark 1 has won, or 0 if his opponent won

        """
        turn=np.random.randint(0,2,size=1)
        if turn.mean()==0:
            self.turn_monitor=0
        elif turn.mean()==1:
            self.turn_monitor=1
        return self.turn_monitor

    def move(self,player,coord):
        
        """Function to perform the action of placing a mark on the tic tac toe board
        After performing the action, this function flips the value of the turn_monitor to 
        the next player

        Args:
        player: 1 if player who is assigned the mark 1 is performing the action, 
        0 if his opponent is performing the action
        coord: The coordinate where the 1 or 0 is to be placed on the 
        tic-tac-toe board (numpy array)

        Returns:
        game_status(): Calls the game status function and returns its value
        board: Returns the new board state after making the move

        """
        if self.board[coord]!=2 or self.game_status()!="In Progress" or self.turn_monitor!=player:
            raise ValueError("Invalid move")
        self.board[coord]=player
        self.turn_monitor=1-player
        return self.game_status(),self.board


    def get_game_state(self):
        
        """Function to check the current status of the game, 
        whether the game has been won, drawn or is in progress

        Args:

        Returns:
        "Won" if the game has been won, "Drawn" if the 
        game has been drawn, or "In Progress", if the game is still in progress

        """
        #check for a win along rows
        for i in range(self.board.shape[0]):
            if 2 not in self.board[i,:] and len(set(self.board[i,:]))==1:
                return "Won"
        #check for a win along columns
        for j in range(self.board.shape[1]):
            if 2 not in self.board[:,j] and len(set(self.board[:,j]))==1:
                return "Won"
        # check for a win along diagonals
        if 2 not in np.diag(self.board) and len(set(np.diag(self.board)))==1:
            return "Won"
        if 2 not in np.diag(np.fliplr(self.board)) and len(set(np.diag(np.fliplr(self.board))))==1:
            return "Won"
        # check for a Draw
        if not 2 in self.board:
            return "Drawn"
        else:
            return "In Progress"
        
        
    def row_winning_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan rowwise and identify coordinate amongst the legal coordinates that will
        result in a winning board state

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent
        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            #check for a win along rows
            for i in range(current_board_state_copy.shape[0]):
                if 2 not in current_board_state_copy[i,:] and len(set(current_board_state_copy[i,:]))==1:
                    selected_move=legal_move_coord
                    return selected_move
            
    def column_winning_move_check(current_board_state,legal_moves_dict,turn_monitor):
        
        """Function to scan column wise and identify coordinate amongst the legal coordinates that will
        result in a winning board state

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move

        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent
        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            for j in range(current_board_state_copy.shape[1]):
                        if 2 not in current_board_state_copy[:,j] and len(set(current_board_state_copy[:,j]))==1:
                            selected_move=legal_move_coord
                            return selected_move

    def diag1_winning_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan diagonal and identify coordinate amongst the legal coordinates that will
        result in a winning board state

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move

        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            if 2 not in np.diag(current_board_state_copy) and len(set(np.diag(current_board_state_copy)))==1:
                selected_move=legal_move_coord
                return selected_move
            
    def diag2_winning_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan second diagonal and identify coordinate amongst the legal coordinates that will
        result in a winning board state

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move

        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            if 2 not in np.diag(np.fliplr(current_board_state_copy)) and len(set(np.diag(np.fliplr(current_board_state_copy))))==1:
                selected_move=legal_move_coord
                return selected_move
            


    def row_block_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan rowwise and identify coordinate amongst the legal coordinates 
        that will prevent the program 
        from winning

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            for i in range(current_board_state_copy.shape[0]):
                if 2 not in current_board_state_copy[i,:] and (current_board_state_copy[i,:]==1).sum()==2:
                    if not (2 not in current_board_state[i,:] and (current_board_state[i,:]==1).sum()==2):
                        selected_move=legal_move_coord
                        return selected_move
            
    def column_block_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan column wise and identify coordinate amongst the legal coordinates that will prevent 1 
        from winning

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            
            for j in range(current_board_state_copy.shape[1]):
                        if 2 not in current_board_state_copy[:,j] and (current_board_state_copy[:,j]==1).sum()==2:
                            if not (2 not in current_board_state[:,j] and (current_board_state[:,j]==1).sum()==2):
                                selected_move=legal_move_coord
                                return selected_move

    def diag1_block_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan diagonal 1 and identify coordinate amongst the legal coordinates that will prevent 1 
        from winning

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor    
            if 2 not in np.diag(current_board_state_copy) and (np.diag(current_board_state_copy)==1).sum()==2:
                    if not (2 not in np.diag(current_board_state) and (np.diag(current_board_state)==1).sum()==2):
                        selected_move=legal_move_coord
                        return selected_move
                
    def diag2_block_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan second diagonal wise and identify coordinate amongst the legal coordinates that will
        result in a column having only 0s

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            if 2 not in np.diag(np.fliplr(current_board_state_copy)) and (np.diag(np.fliplr(current_board_state_copy))==1).sum()==2:
                if not (2 not in np.diag(np.fliplr(current_board_state)) and (np.diag(np.fliplr(current_board_state))==1).sum()==2):
                    selected_move=legal_move_coord
                    return selected_move

    #---------------#
    def row_second_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan rowwise and identify coordinate amongst the legal coordinates that will
        result in a row having two 0s and no 1s

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            
            for i in range(current_board_state_copy.shape[0]):
                if 1 not in current_board_state_copy[i,:] and (current_board_state_copy[i,:]==0).sum()==2:
                    if not (1 not in current_board_state[i,:] and (current_board_state[i,:]==0).sum()==2):
                        selected_move=legal_move_coord
                        return selected_move
            
    def column_second_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan column wise and identify coordinate amongst the legal coordinates that will
        result in a column having two 0s and no 1s

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            
            for j in range(current_board_state_copy.shape[1]):
                        if 1 not in current_board_state_copy[:,j] and (current_board_state_copy[:,j]==0).sum()==2:
                            if not (1 not in current_board_state[:,j] and (current_board_state[:,j]==0).sum()==2):
                                selected_move=legal_move_coord
                                return selected_move

    def diag1_second_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan diagonal wise and identify coordinate amongst the legal coordinates that will
        result in a column having two 0s and no 1s

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            if 1 not in np.diag(current_board_state_copy) and (np.diag(current_board_state_copy)==0).sum()==2:
                if not (1 not in np.diag(current_board_state) and (np.diag(current_board_state)==0).sum()==2):
                    selected_move=legal_move_coord
                    return selected_move
                
    def diag2_second_move_check(current_board_state,legal_moves_dict,turn_monitor):
        """Function to scan second diagonal wise and identify coordinate amongst 
        the legal coordinates that will result in a column having two 0s and no 1s

        Args:
        legal_moves_dict: Dictionary of legal next moves
        turn_monitor: whose turn it is to move
        
        Returns:
        selected_move: The coordinates of numpy array where opponent places their mark

        """ 
        legal_move_coords =  list(legal_moves_dict.keys())
        random.shuffle(legal_move_coords)
        for legal_move_coord in legal_move_coords:
            current_board_state_copy=current_board_state.copy()
            current_board_state_copy[legal_move_coord]=turn_monitor
            if 1 not in np.diag(np.fliplr(current_board_state_copy)) and (np.diag(np.fliplr(current_board_state_copy))==0).sum()==2:
                if not (1 not in np.diag(np.fliplr(current_board_state)) and (np.diag(np.fliplr(current_board_state))==0).sum()==2):
                    selected_move=legal_move_coord
                    return selected_move
        
    def opponent_move_selector(current_board_state,turn_monitor,mode):
        
        """Function that picks a legal move for the opponent

        Args:
        current_board_state: Current board state
        turn_monitor: whose turn it is to move
        mode: whether hard or easy mode

        Returns:
        selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

        """ 
        legal_moves_dict=legal_moves_generator(current_board_state,turn_monitor)
        
        winning_move_checks=[row_winning_move_check,column_winning_move_check,diag1_winning_move_check,diag2_winning_move_check]
        block_move_checks=[row_block_move_check,column_block_move_check,diag1_block_move_check,diag2_block_move_check]
        second_move_checks=[row_second_move_check,column_second_move_check,diag1_second_move_check,diag2_second_move_check]

        if mode=="Hard":
            random.shuffle(winning_move_checks)
            random.shuffle(block_move_checks)
            random.shuffle(second_move_checks)        
            
            for fn in winning_move_checks:
                if fn(current_board_state,legal_moves_dict,turn_monitor):
                    return fn(current_board_state,legal_moves_dict,turn_monitor)
                
            for fn in block_move_checks:
                if fn(current_board_state,legal_moves_dict,turn_monitor):
                    return fn(current_board_state,legal_moves_dict,turn_monitor)
                
            for fn in second_move_checks:
                if fn(current_board_state,legal_moves_dict,turn_monitor):
                    return fn(current_board_state,legal_moves_dict,turn_monitor)
                
            selected_move=random.choice(list(legal_moves_dict.keys()))
            return selected_move
        
        elif mode=="Easy":
            legal_moves_dict=legal_moves_generator(current_board_state,turn_monitor)
            selected_move=random.choice(list(legal_moves_dict.keys()))
            return selected_move
        
        
    