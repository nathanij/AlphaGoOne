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
                 exploration_factor: int, search_limit: int,
                 expansion_limit: int):
        self.policy_network_ = policy_network
        self.value_network_ = value_network
        self.root_ = root
        self.exploration_factor_ = exploration_factor
        self.iterations_ = 0
        self.search_limit_ = search_limit
        self.expansion_limit_ = expansion_limit


    def finished(self):
        return self.iterations_ >= self.search_limit_
    
    def exploration_score(self, move: int, policy_score: float) -> float:
        return 0
    
    def expand(self):
        cur = self.root_
        while not cur.is_leaf():
            cur.add_visit()
            branches = cur.branches()
            if cur.get_active_player() == 0:  # black so maximize
                max_value = -float('inf')
                best_child = None
                for move in branches:
                    child = cur.child_at(move)
                    q = child.average_value()  # TODO: redo with medium article
                    u = self.exploration_score(child)  # TODO: build, also change interface for this probably
                    if q + u > max_value:
                        max_value = q + u
                        best_child = child
                cur = best_child
            else:  # white so minimize
                min_value = float('inf')
                best_child = None
                for move in branches:
                    child = cur.child_at(move)
                    q = child.average_value()
                    u = self.exploration_score(child)
                    if q + u < min_value:
                        min_value = q + u
                        best_child = child
                cur = best_child
        
        for move, strength, state in self.explore(cur):  # TODO: build (get sorted list of strengths, while len < limit check if legal and append triplet)
            child = cur.add_child(move, strength, state)  # TODO: build (this should return the searchnode), store strength inside 
            self.evaluate(child)  # TODO: build (evaluates new state and sets it within the searchnode)
        while cur != self.root_:
            cur.reevaluate()  # TODO: build
            cur = cur.ascend()  # TODO: build
    