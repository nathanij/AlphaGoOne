from game_state import GameState
from test_engine import TestEngine
import time


class Driver:
    # Reps board as -1 for black, 0 for empty, 1 for white
    def __init__(self, size = 19):
        self.state_ = GameState(size)
        self.engine_ = TestEngine()

    def drive(self):
        setup_start = time.time()
        self.reset()
        setup_t = time.time() - setup_start
        print(f"Setup time: {setup_t}")
        elapsed = 0
        turns = 0
        for i in range(2000, 2500):
            count = 0
            start_time = time.time()
            # value network will always be from the perspective of black
            while not self.state_.finished() and count < i:
                active = self.state_.get_active_player()
                player_state = self.state_.get_player_state(active)
                result = False
                while not result:
                    move = self.engine_.move(player_state)
                    result = self.state_.make_move(move)
                self.engine_.reset_valid()
                count += 1
            elapsed += time.time() - start_time
            turns += count
            self.reset()
        print(f"Average time of turn simulation = {(elapsed) / turns} seconds")

    def reset(self):
        self.state_ = GameState()
