import os


import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten



def build_model(num_dense_units, verbose=0):
    
    model = Sequential()
    model.add(Dense(num_dense_units, input_dim=9,kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(num_dense_units, kernel_initializer='normal',activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(1,kernel_initializer='normal'))

    model.compile( optimizer='adam',
                  loss='mse')
    if verbose:
        model.summary()
        
    return model


    
def opponent_move_selector(current_board_state,turn,mode):
    """Function that picks a legal move for the opponent

    Args:
    current_board_state: Current board state
    turn: whose turn it is to move
    mode: whether hard or easy mode

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

    """ 
    legal_moves_dict=legal_moves_generator(current_board_state,turn)
    
    winning_move_checks=[row_winning_move_check,column_winning_move_check,diag1_winning_move_check,diag2_winning_move_check]
    block_move_checks=[row_block_move_check,column_block_move_check,diag1_block_move_check,diag2_block_move_check]
    second_move_checks=[row_second_move_check,column_second_move_check,diag1_second_move_check,diag2_second_move_check]

    if mode=="Hard":
        random.shuffle(winning_move_checks)
        random.shuffle(block_move_checks)
        random.shuffle(second_move_checks)        
        
        for fn in winning_move_checks:
            if fn(current_board_state,legal_moves_dict,turn):
                return fn(current_board_state,legal_moves_dict,turn)
            
        for fn in block_move_checks:
            if fn(current_board_state,legal_moves_dict,turn):
                return fn(current_board_state,legal_moves_dict,turn)
            
        for fn in second_move_checks:
            if fn(current_board_state,legal_moves_dict,turn):
                return fn(current_board_state,legal_moves_dict,turn)
            
        selected_move=random.choice(list(legal_moves_dict.keys()))
        return selected_move
    
    elif mode=="Easy":
        legal_moves_dict=legal_moves_generator(current_board_state,turn)
        selected_move=random.choice(list(legal_moves_dict.keys()))
        return selected_move

def train_model(model,mode,game,print_progress=False):

    """
    Args:
    model: The Evaluator function being trained

    Returns:
    model: The model updated using SGD
    y: The corrected scores

    """ 
    # start the game
    if print_progress==True:
        print("___________________________________________________________________")
        print("Starting a new game")
    #game=tic_tac_toe_game()
    
    scores_list=[]
    corrected_scores_list=[]
    new_board_states_list=[]
    
    while(1):
        if game.get_board_state()=="In Progress" and game.turn==1:
            # If its the program's turn, use the Move Selector function to select the next move
            selected_move,new_board_state,score=move_selector(model,game.board,game.turn)
            scores_list.append(score[0][0])
            new_board_states_list.append(new_board_state)
            # Make the next move
            game_status,board=game.move(game.turn,selected_move)
            if print_progress==True:
                print("Program's Move")
                print(board)
                print("\n")
        elif game.game_status()=="In Progress" and game.turn==0:
            selected_move=opponent_move_selector(game.board,game.turn,mode=mode)
        
            # Make the next move
            game_status,board=game.move(game.turn,selected_move)
            if print_progress==True:
                print("Opponent's Move")
                print(board)
                print("\n")
        else:
            break

    
    # Correct the scores, assigning 1/0/-1 to the winning/drawn/losing final board state, 
    # and assigning the other previous board states the score of their next board state
    new_board_states_list=tuple(new_board_states_list)
    new_board_states_list=np.vstack(new_board_states_list)
    if game_status=="Won" and (1-game.turn)==1: 
        corrected_scores_list=shift(scores_list,-1,cval=1.0)
        result="Won"
    if game_status=="Won" and (1-game.turn)!=1:
        corrected_scores_list=shift(scores_list,-1,cval=-1.0)
        result="Lost"
    if game_status=="Drawn":
        corrected_scores_list=shift(scores_list,-1,cval=0.0)
        result="Drawn"
    if print_progress==True:
        print("Program has ",result)
        print("\n Correcting the Scores and Updating the model weights:")
        print("___________________________________________________________________\n")
        
    x=new_board_states_list
    y=corrected_scores_list
    
    def unison_shuffled_copies(a, b):
        assert len(a) == len(b)
        p = np.random.permutation(len(a))
        return a[p], b[p]
    
    # shuffle x and y in unison
    x,y=unison_shuffled_copies(x,y)
    x=x.reshape(-1,9) 
    
    # update the weights of the model, one record at a time
    model.fit(x,y,
            epochs=1,
            batch_size=1,
            verbose=0)
    return model,y,result


def make_move(model,current_board_state,turn):
    """Function that selects the next move to make from a set of possible legal moves

    Args:
    model: The Evaluator function to use to evaluate each possible next board state
    turn: 1 if it's the player who places the mark 1's turn to play, 0 if its his opponent's turn

    Returns:
    selected_move: The numpy array coordinates where the player should place thier mark
    new_board_state: The flattened new board state resulting from performing above selected move
    score: The score that was assigned to the above selected_move by the Evaluator (model)

    """
    tracker={}
    legal_moves_dict=legal_moves_generator(current_board_state,turn)
    for legal_move_coord in legal_moves_dict:
        score=model.predict(legal_moves_dict[legal_move_coord].reshape(1,9))
        tracker[legal_move_coord]=score
    selected_move=max(tracker, key=tracker.get)
    new_board_state=legal_moves_dict[selected_move]
    score=tracker[selected_move]
    return selected_move,new_board_state,score

if __name__ == '__main__':
    
    # Check model params
    build_model(100, verbose=1)