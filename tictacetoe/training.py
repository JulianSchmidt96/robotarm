
import os 
from services.gameManager import GameManager
from models.game import Game
import dlmodel as dlm
from moves import *
from scipy.ndimage.interpolation import shift


def modelmove(model, board, player):
    """AI is creating summary for modelmove

    Args:
        model ([keras]): [keras model]
        board ([np array]): board as matrix nan values are fields that are not yet taken
        player ([bool]): [0 or 1 (player annot)]
    """
    pass

def move_selector(model,current_board_state,turn,verbose=0):
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
        score=model.predict(legal_moves_dict[legal_move_coord].reshape(1,9,verbose=verbose))
        tracker[legal_move_coord]=score
    selected_move=max(tracker, key=tracker.get)
    new_board_state=legal_moves_dict[selected_move]
    score=tracker[selected_move]
    return selected_move,new_board_state,score
    
def train(model,game, verbose=0):
    """Function trains the Evaluator (model) by playing a game against an opponent 
    playing random moves, and updates the weights of the model after the game
    
    Note that the model weights are updated using SGD with a batch size of 1

    Args:
    model: The Evaluator function being trained

    Returns:
    model: The model updated using SGD
    y: The corrected scores

    """ 
    # start the game
   
    gamemanager=GameManager(game)
    
    scores_list=[]
    corrected_scores_list=[]
    new_board_states_list=[]
    
    while(1):
        if gamemanager.get_board_state()=="In Progress" and game.turn==1:
            # If its the program's turn, use the Move Selector function to select the next move
            selected_move,new_board_state,score=move_selector(model,game.board,game.turn)
            
            scores_list.append(score[0][0])
            new_board_states_list.append(new_board_state)
            # Make the next move
            gamemanager.get_board_state(),
            game.set(selected_move)
        
            
        elif gamemanager.get_board_state()=="In Progress" and game.turn==0:
            selected_move=opponent_move_selector(game.board,game.turn)
        
            # Make the next move
            gamemanager.get_board_state()
            game.set(selected_move)
           
        else:
            break

    
    # Correct the scores, assigning 1/0/-1 to the winning/drawn/losing final board state, 
    # and assigning the other previous board states the score of their next board state
    new_board_states_list=tuple(new_board_states_list)
    new_board_states_list=np.vstack(new_board_states_list)
    if gamemanager.get_board_state()=="Won" and (1-game.turn)==1: 
        corrected_scores_list=shift(scores_list,-1,cval=1.0)
        result="Won"
        
    if gamemanager.get_board_state()=="Won" and (1-game.turn)!=1:
        corrected_scores_list=shift(scores_list,-1,cval=-1.0)
        result="Lost"
    if gamemanager.get_board_state()=="Drawn":
        corrected_scores_list=shift(scores_list,-1,cval=0.0)
        result="Drawn"
    
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
              verbose=verbose)
    
    return model,y,result
 
def unison_shuffled_copies(a, b):
        assert len(a) == len(b)
        p = np.random.permutation(len(a))
        return a[p], b[p]
    
if __name__ == '__main__':
    
    # Weak Model
    
    weak_model = dlm.build_model(10)
    
    game = Game()


    print(f' testing toss : start-player is : {game.toss()}')
        
    print(' ')
    
    
    train(weak_model, game, game.turn)
    