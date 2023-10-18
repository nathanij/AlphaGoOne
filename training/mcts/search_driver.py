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
                 search_limit: int, expansion_factor: int, active_player: int):
        self.policy_network_ = policy_network
        self.value_network_ = value_network
        self.root_ = root
        self.iterations_ = 0
        self.search_limit_ = search_limit
        self.expanison_factor_ = expansion_factor
        self.active_player_ = active_player


    def finished(self):
        return self.iterations_ >= self.search_limit_
    
    def expand(self):
        # while not at a leaf node: (i.e. len(children) != 0)
            # increment visit count
            # Each child will have an evaluation (Q) and an exploitation (U)
            # If black to move, select maximum of Q+U, else minimum (i.e. max(-Q-U))
            # Move down to selected node
        # once at lead node (including initial iteration)
        # sort policy network results, generate board states for the top {expansion_factor} legal ones
        # for each child, set visit count to 1, evaluate with value network (store natively in node)
        # traverse up the tree back to the root
        # at each node, refactor the nodes average value (unweighted average of children + self)
        pass
    