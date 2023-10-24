import numpy as np

from mcts.board_state import BoardState
from mcts.search_driver import SearchDriver
from networks.value_network import ValueNetwork
from networks.policy_network import PolicyNetwork
from mcts.search_node import SearchNode


class SimDriver:
    def __init__(self, policy_network_path: str, value_network_path: str,
                 exploration_factor: int, search_limit: int,
                 expansion_limit: int):
        self.policy_network_ = PolicyNetwork(policy_network_path)
        self.value_network_ = ValueNetwork(value_network_path)
        self.root_ = SearchNode(None, BoardState(), 0)
        self.exploration_factor_ = exploration_factor
        self.search_limit_ = search_limit
        self.expansion_limit_ = expansion_limit
        self.training_states_ = []
        self.visit_counts_ = []

    def reset(self):
        self.root_ = SearchNode(None, BoardState())
        self.training_states_ = []
        self.visit_counts_ = []

    def training_states(self) -> np.ndarray:
        return np.vstack(self.training_states_)
    
    def result_tags(self) -> np.array:
        val = self.root_.result()  # 1 for white win, 0.5 for draw, 0 for black win  TODO: build
        return np.full(len(self.training_states_), val)
    
    def policy_tags(self) -> np.ndarray:
        return np.vstack(self.visit_counts_)
    
    # Tree structuring:
    # Root node passed into search_driver
    # After the end of search, root is updated to the most visited child
    # Root has a .finished() method, that is used instead of an exterior game state
    # THis is accessible via the simulation driver
    # It returns the new state object to be put into the generated leaf

    def simulate(self):
        self.reset()
        while not self.root_.finished():
            pre_state = self.root_.get_flattened_state()
            active_player = self.root_.get_active_player()
            pre_state.append(active_player)
            self.training_states_.append(np.array(pre_state))
            search_driver = SearchDriver(self.policy_network_,
                                         self.value_network_, self.root_,
                                         self.exploration_factor_,
                                         self.search_limit_,
                                         self.expansion_limit_)
            while not search_driver.finished():
                search_driver.expand()
            move = search_driver.most_visited()  # TODO: build
            self.root_ = self.root_.new_root_from(move)  # TODO: build
            self.visit_counts_.append(search_driver.normalized_visit_count())  # TODO: build
