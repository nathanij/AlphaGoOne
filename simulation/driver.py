from simulation.game_state import GameState
from simulation.test_engine import TestEngine
import time


class Driver:
    # Reps board as -1 for black, 0 for empty, 1 for white
    def __init__(self):
        self.state_ = GameState()
        self.engine_ = TestEngine()
        self.active_ = 0 # signifying it's black's turn

    def drive(self):
        start_time = time.time()
        # value network will always be from the perspective of black
        while not self.state_.finished():
            player_state = self.state_.get_player_state(self.active_)
            result = False
            while not result:
                move = self.engine_.make_move(player_state)
                result = self.state_.make_move(move)
            self.engine_.reset_valid()
            self.active_ = not self.active_

        print(f'Total time elapsed: {(start_time - time.time())}')
