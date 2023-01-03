import os
import torch
import numpy as np
from flask import Flask, jsonify, request
from flask_cors import cross_origin

from models.net import TicTacToeNet

app = Flask(__name__)

def convert_symbol(symbol):
    if symbol == "X":
        return 1
    elif symbol == "O":
        return 2
    else:
        return 0



def convert_board_to_numpy(board):
    nboard = [int(i) for i in board]
    return np.array(nboard)



@app.route("/api", methods=["GET"])
@cross_origin()
def get_prediction():
    # Get the board from the query parameters
    
    player = request.args.get("player")

    player = convert_symbol(player)

    if player == 0:
        return "invalid player"

    # Convert the board to a numpy array
    board = request.args.get("board")
    print("board", board)
    print(len(board))
    board = convert_board_to_numpy(board.split(','))
    print("nboard", board)
    print(len(board))


    # Berechne Logits für alle möglichen Züge
    board = torch.from_numpy(board).float()
    

    
    mask = torch.tensor((board != 0), dtype=torch.bool)
    
    # Convert the player string to a tensor
    player = torch.tensor(player, dtype=torch.long)
    
    model = get_model(player.item())

    # Stack the board and player tensors along the channel dimension
    

    # Pass the input tensor to the model

    logits = model(board.unsqueeze(0))
    

    # Set the logits for the other player's moves to zero
    logits[:, player == 0] = 0

    # Calculate the softmax probabilities for the valid moves
    probs = torch.softmax(logits, dim=1)
    probs[:,mask] = 0



    # Choose the highest probability move
    action = torch.argmax(probs).item()
    
    prediction = action // 3, action % 3
    print("preditction is : row = ", prediction[0], "column = ", prediction[1])
    return jsonify({'prediction': prediction})



@app.route('/')
def index():
    return 'working'

def get_model(player):

    model = TicTacToeNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE).to(DEVICE)
    if player == 1:
        model.load_state_dict(torch.load("models/saved_models/model1.pt"))
    elif player == 2:
        model.load_state_dict(torch.load("models/saved_models/model2.pt"))
    else:
        raise ValueError("Invalid player value")
    return model


if __name__ == '__main__':
    
    
    INPUT_SIZE = 9
    HIDDEN_SIZE = 16
    OUTPUT_SIZE = 9
    DEVICE = "cpu"
    
    app.run()
