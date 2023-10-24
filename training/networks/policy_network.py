from typing import List, Tuple
import numpy as np
import pytorch
from mcts.board_state import BoardState

class PolicyNetwork:
    def __init__(self, weight_path: str):
        self.weight_path_ = weight_path
        self.network_ = pytorch.load(weight_path)  # TODO: look up equivalent pytorch method

    def refresh(self):
        self.network_ = pytorch.load(self.weight_path_)

    def eval(self, state: BoardState) -> List[Tuple[float, int]]:
        position = state.get_flattened_state()
        policy = self.network_.eval(np.array(position))
        pairings = []
        for move, strength in enumerate(policy):
            pairings.append((strength, move))
        pairings.sort(key = lambda x: (x[0], -x[1]), reverse = True)  # Descending strength, ascending move order
        return pairings
