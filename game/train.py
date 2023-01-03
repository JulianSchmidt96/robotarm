import numpy as np
import torch
import torch.nn.functional as F

from tictactoe import TicTacToe
from models.net import TicTacToeNet
from players import AIPlayer






def play_game_with_reward(player1, player2, reward_function):
    game = TicTacToe(player1, player2)
    result = game.play()
    result = result[1]
    if result == 1:
        return reward_function( 1), game.board
    elif result == 2:
        return reward_function( 2), game.board
    else:
        return reward_function( 0), game.board

def train_with_reward(num_games, model1, model2, optimizer1, optimizer2, device, reward_function):
    for i in range(num_games):
        # Spielen
        reward, board = play_game_with_reward(model1, model2, reward_function)


            # Gewinner bestimmen
        if reward == 1:
            winner = model1
            loser = model2
            optimizer = optimizer1
        elif reward == -1:
            winner = model2
            loser = model1
            optimizer = optimizer2
        else:
            continue  # unentschieden, keine Anpassung der Modelle notwendig
        print(f"reward is {reward}")
        print("board is : ")
        print(board)

        model1_loss, model2_loss = compute_loss(model1.model, model2.model, board)

        if model1_loss > model2_loss:
            optimizer.zero_grad()
            model1_loss.backward()
            optimizer.step()
        else:
            optimizer.zero_grad()
            model2_loss.backward()
            optimizer.step()


        # Modelle speichern

        torch.save(model1.model.state_dict(), "models/saved_models/model1.pt")
        torch.save(model2.model.state_dict(), "models/saved_models/model2.pt")
        print(f"Training {i+1} beendet!")


def compute_loss(model1, model2, board):
    # Verlust des ersten Modells berechnen
    model1_logits = model1(torch.tensor(board, dtype=torch.float).view(1, -1))
    model1_loss = F.cross_entropy(model1_logits, torch.tensor([1]))

    # Verlust des zweiten Modells berechnen
    model2_logits = model2(torch.tensor(board, dtype=torch.float).view(1, -1))
    model2_loss = F.cross_entropy(model2_logits, torch.tensor([0]))

    return model1_loss, model2_loss


def reward_function( winner):
    if winner == 1:
        return 1
    elif winner == 2:
        return -1
    else:
        return 0



 

    
if __name__ == "__main__":
    # Modelle instanziieren
    INPUT_SIZE = 9
    HIDDEN_SIZE = 16
    OUTPUT_SIZE = 9
    DEVICE = "cpu"
    model1 = TicTacToeNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE).to(DEVICE)
    model2 = TicTacToeNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE).to(DEVICE)

    # Optimizer instanziieren
    LEARNING_RATE = 0.01
    optimizer1 = torch.optim.Adam(model1.parameters(), lr=LEARNING_RATE)
    optimizer2 = torch.optim.Adam(model2.parameters(), lr=LEARNING_RATE)

    player_1 = AIPlayer(model1)
    player_2 = AIPlayer(model2)
    # Training starten
    NUM_GAMES = 300000
    train_with_reward(NUM_GAMES, player_1, player_2, optimizer1, optimizer2, DEVICE,reward_function)
    
