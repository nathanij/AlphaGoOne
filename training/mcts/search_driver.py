import math
from typing import List, Tuple
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
    
    def exploration_score(self, parent: SearchNode, child: SearchNode) -> float:
        scalar = self.exploration_factor_ * child.policy_score()
        visit_score = math.sqrt(parent.visits() + parent.num_children()) / (1 + child.visits())
        return scalar * visit_score
    
    def explore(self, cur: SearchNode) -> List[Tuple[float, int, SearchNode]]:  # TODO: check typing here
        move_strengths = self.policy_network_.eval(cur)
        i = 0
        candidates = []
        while i < len(move_strengths) and len(candidates) < self.expansion_limit_:
            move = move_strengths[i][1]
            result = cur.state().make_move(move)  # TODO: refactor to return None if failed, else a new Boardstate with the move made
            if result is not None:
                candidates.append(move_strengths[i][0], move, result)
        return candidates
    
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
                    q = child.average_value()
                    u = self.exploration_score(cur, child)
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
                    u = self.exploration_score(cur, child)
                    if q + u < min_value:
                        min_value = q + u
                        best_child = child
                cur = best_child
        
        for strength, move, state in self.explore(cur):  # TODO: build (get sorted list of strengths, while len < limit check if legal and append triplet)
            child = cur.add_child(move, strength, state)  # TODO: build (this should return the searchnode), store strength inside 
            self.evaluate(child)  # TODO: build (evaluates new state and sets it within the searchnode)
        while cur != self.root_:
            cur.reevaluate()  # TODO: build
            cur = cur.ascend()  # TODO: build
    