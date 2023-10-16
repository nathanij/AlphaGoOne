import numpy as np

from typing import List

from game_state import GameState
from mcts.search_driver import SearchDriver
from mcts.search_tree_header import SearchTreeHeader
from networks.value_network import ValueNetwork
from networks.policy_network import PolicyNetwork


class SimDriver:
    def __init__(self, policy_network_path: str, value_network_path: str,
                 search_limit: int):
        self.policy_network_ = PolicyNetwork(policy_network_path)
        self.value_network_ = ValueNetwork(value_network_path)
        self.search_limit_ = search_limit
        self.game_state_ = GameState()
        self.training_states_ = []
        self.visit_counts_ = []

    def reset(self):
        self.game_state_ = GameState()
        self.training_states_ = []
        self.visit_counts_ = []

    def training_states(self) -> np.ndarray:
        return np.vstack(self.training_states_)
    
    def result_tags(self) -> np.array:
        val = self.game_state_.result()  # 1 for white win, 0.5 for draw, 0 for black win
        return np.full(len(self.training_states_), val)
    
    def policy_tags(self) -> np.ndarray:
        return np.vstack(self.visit_counts_)

    def simulate(self):
        self.reset()
        tree = SearchTreeHeader()
        while not self.game_state_.finished():
            pre_state = self.game_state_.get_flattened_state()  # TODO: build
            active_player = self.game_state_.get_active_player()
            pre_state.append(active_player)
            self.training_states_.append(pre_state)
            search_driver = SearchDriver(tree, self.search_limit_, active_player)
            while not search_driver.finished():
                move = search_driver.expand()  # TODO: build
                # continue move processing logic here
            self.visit_counts_.append(search_driver.normalized_visit_count())  # TODO: build
