from services.gameManager import GameManager
from models.game import Game

game = Game()


print(f' testing toss : start-player is : {game.toss()}')
      
print(' ')
gameManager = GameManager(game.board, game.turn)


print(' testing board_state_request -> inital board_state is :')
print(f'{gameManager.get_board_state()}')
print(' ')

print(f' testing legal_moves_generator -> legal moves are : {gameManager.legal_moves_generator()}')

game.set([0,1],1)

print(f'{gameManager.get_board_state()}')