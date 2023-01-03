import numpy as np
import torch

class HumanPlayer:
    def get_action(self, board):
        self.board = board
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    action = (row, col)
                    if board[action] == 0:
                        print("check")
                        return row * 3 + col
                    else:
                        print("Field already occupied, try again.")
                else:
                    print("Invalid input, try again.")
            except ValueError:
                print("Invalid input, try again.")
            
            

                
class AIPlayer:
    def __init__(self, model):
        self.model = model
        #self.board = None
    def get_action(self, board):
        # Flatten board
        
        board = np.array(board).flatten()
        
        # Berechne Logits für alle möglichen Züge
        board = torch.from_numpy(board).float()
        logits = self.model(board.unsqueeze(0))
        
        mask = torch.tensor((board != 0), dtype=torch.bool)
        
        #logits[:,mask] = 0
       
        board[mask] = 0


        # Berechne Softmax-Werte für alle möglichen Züge
        probs = torch.softmax(logits, dim=1)
        probs[:,mask] = 0

        # Wähle den am höchsten bewerteten Zug aus
        action = torch.argmax(probs)
        
        

        # Gib den Index des gewählten Zugs zurück
        return action










