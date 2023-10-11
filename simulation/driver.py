from game_state import GameState
from test_engine import TestEngine
import time


class Driver:
    # Reps board as -1 for black, 0 for empty, 1 for white
    def __init__(self, size = 19):
        self.state_ = GameState(size)
        self.engine_ = TestEngine()

    def drive(self):
        start_time = time.time()
        # value network will always be from the perspective of black
        while not self.state_.finished():
            active = self.state_.get_active_player()
            player_state = self.state_.get_player_state(active)
            result = False
            while not result:
                move = self.engine_.move(player_state)
                result = self.state_.make_move(move)
            self.engine_.reset_valid()

        print(f'Total time elapsed: {(time.time() - start_time)}')

    def reset(self):
        self.state_ = GameState()
