import numpy as np

class TurnMonitor():
    
    def __init(self):
        self.turn
    
    def toss(self):
        
        """Function to simulate a toss and decide which player goes first

        Args:

        Returns:
        Returns 1 if player assigned mark 1 has won, or 0 if his opponent won

        """
        turn=np.random.randint(0,2,size=1)
        if turn.mean() == 0:
            self.turn_monitor = 'A'
        elif turn.mean() == 1:
            self.turn_monitor = 'B'
        return self.turn_monitor