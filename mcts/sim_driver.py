from game_state import GameState
from networks.value_network import ValueNetwork
from networks.policy_network import PolicyNetwork


class SimDriver:
    def __init__(self, policy_network_path, value_network_path):
        self.policy_network_ = PolicyNetwork(policy_network_path)
        self.value_network_ = ValueNetwork(value_network_path)
        self.state_ = GameState()
        self.tree_ = 
