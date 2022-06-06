from services.gameManager import GameManager
from models.game import Game

game = Game()


print(f' testing toss : start-player is : {game.toss()}')
      
      
gameManager = GameManager(game.board, game.turn)


print(' testing board_state_request -> inital board_state is :')
print(f'{gameManager.get_board_state()}')