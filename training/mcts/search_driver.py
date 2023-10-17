from mcts.search_node import SearchNode
from networks.policy_network import PolicyNetwork
from networks.value_network import ValueNetwork


class SearchDriver:
    # Minimize instead of maximize if black is moving
    # For search, illegal moves should not be considered
    # This will train the engine not to make them either (as training policy 
    # vector will not include any)
    def __init__(self, policy_network: PolicyNetwork, 
                 value_network: ValueNetwork, root: SearchNode,
                 search_limit: int, active_player: int):
        self.policy_network_ = policy_network
        self.value_network_ = value_network
        self.root_ = root
        self.active_player_ = active_player
        self.iterations_ = 0
        self.search_limit_ = search_limit

    def finished(self):
        return self.iterations_ >= self.search_limit_
    
    def expand(self):
        pass
    
    # For our tree search expansion algorithm
    # Update visits counts on the way down the tree
    # Back up value scores on the way back up to the root
    