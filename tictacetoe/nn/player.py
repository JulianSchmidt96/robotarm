import torch
import torch.nn as nn
import torch.optim as optim

class Player:
    def __init__(self, marker, model):
        self.marker = marker
        self.model = model

    def make_move(self, board):
        # Use the model to predict the best move based on the current board state
        with torch.no_grad():
            input = self.preprocess_board(board)
            logits = self.model(input)
            action = logits.argmax().item()
            row = action // 3
            col = action % 3
            return row, col

    def preprocess_board(self, board):
       return torch.tensor([1 if space == self.marker else -1 if space != ' ' else 0 for row in board for space in row], dtype=torch.float32)

