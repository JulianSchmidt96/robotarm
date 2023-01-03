import numpy as np
import torch

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = np.zeros((3, 3))
        self.players = [player1, player2]
        self.current_player = 0

    

    def play(self):
        #print(self.board)
        
        while not self.game_over():
        # Spieler macht Zug
            action = self.players[self.current_player].get_action(self.board)
           
            #print(type(action))
            row, col = action // 3, action % 3
            #print("board before placement:")
            
            self.board[row][col] = self.current_player + 1
            
            #print(self.board)
            #print("player just placed is : ", self.winner())
            #print("player is : ", self.current_player)
            #print("board after placement : ")
            #print(self.board)
            
           
            self.current_player = (self.current_player + 1) % 2
            

        return self.board, self.winner()
            
            

        







    def game_over(self):
        # Kontrolliert ob das Spiel beendet ist
        for i in range(3):
            # Zeilen
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                return True
            # Spalten
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                return True
        # Diagonalen
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[2][0] != 0:
            return True
        # Unentschieden
        if not 0 in self.board:
            return True
        # Das Spiel ist noch nicht beendet
        return False


    
    def winner(self):
        # Gibt den Gewinner des Spiels zurück
        for i in range(3):
            # Zeilen
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                print("winner is last player:")
                return self.board[i][0]
            # Spalten
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                print("winner is last player:")
                return self.board[0][i]
        # Diagonalen
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            print("winner is last player:")
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[2][0] != 0:
            print("winner is last player:")
            return self.board[2][0]
        # Unentschieden
        if not 0 in self.board:
            return 0
        # Das Spiel ist noch nicht beendet
        return -1



