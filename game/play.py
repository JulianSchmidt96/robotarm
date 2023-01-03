import torch

from tictactoe import TicTacToe
from players import HumanPlayer, AIPlayer
from models.net import TicTacToeNet




if __name__ == "__main__":
    # Neuronales Netz instanziieren
    INPUT_SIZE = 9
    HIDDEN_SIZE = 16
    OUTPUT_SIZE = 9
    DEVICE = "cpu"
    model = TicTacToeNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE).to(DEVICE)

    # Modell laden
    model.load_state_dict(torch.load("models/saved_models/model1.pt"))

    # Spieler instanziieren
    player1 = HumanPlayer()
    player2 = AIPlayer(model)

    # Tic Tac Toe-Spiel instanziieren und spielen
    game = TicTacToe(player1, player2)

    # Spiel starten und Ergebnis anzeigen
    result = game.play()
    if result == 0:
        print("Unentschieden!")
    else:
        print(f"Spieler {result} hat gewonnen!")

