import numpy as np
import pytorch
from mcts.board_state import BoardState

class ValueNetwork:
    # Network evaluates the probability of a black win from the given situation
    def __init__(self, weight_path: str):
        self.weight_path_ = weight_path
        self.model_ = pytorch.load(self.address_)  # TODO: correct method

    def refresh(self):
        self.model_ = pytorch.load(self.address_)

    def eval(self, state: BoardState) -> float:
        position = state.get_flattened_state()
        return self.network_.eval(np.array(position))
    