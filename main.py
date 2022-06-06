from services.gameManager import GameManager
from services.turnMonitor import TurnMonitor
from models.game import Game

game = Game()

turnMonitor = TurnMonitor()

gameManager = GameManager(game.board, turnMonitor)

print(gameManager.get_board_state())