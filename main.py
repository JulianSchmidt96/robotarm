from services.gameManager import GameManager
from models.game import Game

game = Game()


print(f' testing toss : start-player is : {game.toss()}')
      
print(' ')
gameManager = GameManager(game)


print(' testing game:state_request -> inital game_state is :')
print(f'{gameManager.get_board_state()}')
print(' ')

print(f' testing legal_moves_generator -> legal moves are : {gameManager.legal_moves_generator()}')

print('testing game set method:')

gameManager.set([0,1])

print(' ')

print('get board state after set method with Game Manager:')
print(' ')
print(f'{gameManager.get_board_state()}')

gameManager.set([0,1])

print(' ')

print('get board state after set method with Game Manager:')
print(' ')
print(f'{gameManager.get_board_state()}')

