import torch
import torch.nn as nn
import torch.optim as optim


class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1


    def play(self):
        while True:
            self.print_board()
            if self.current_player == self.player1:
                row, col = self.player1.make_move(self.board)
            else:
                row, col = self.player2.make_move(self.board)

            # Update the board with the current player's move
            self.board[row][col] = self.current_player.marker

            # Check if the current player won
            if self.player_won():
                self.print_board()
                print(f"Player {self.current_player.marker} won!")
                break

            # Check if the board is full
            if self.board_full():
                self.print_board()
                print("It's a draw!")
                break

            # Switch to the other player
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    
    def board_full(self):
            for row in self.board:
                for space in row:
                    if space == ' ':
                        return False
            return True

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
        print()
    
    
    
    
    
    def player_won(self):
        marker = self.current_player.marker
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] == marker:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] == marker:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] == marker:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] == marker:
            return True

        return False
    







