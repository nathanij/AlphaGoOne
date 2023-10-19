from typing import List, Optional, Type
from board_state import BoardState


class SearchNode:
    def __init__(self, parent: Optional[Type['SearchNode']], state: BoardState,
                 policy_score: float):
        self.parent_ = parent
        self.state_ = state
        self.visits_ = 0
        self.value_ = 0  # determined by the value network, called when the node is made
        self.policy_score_ = policy_score
        self.total_value_ = 0  # cumulative value score (not divided by visits)
        self.num_descendants_ = 0
        self.children_ = dict()

    def finished(self) -> bool:
        return self.state_.finished()
    
    def get_flattened_state(self) -> List[int]:
        return self.state_.get_flattened_state()
    
    def get_active_player(self) -> bool:
        return self.state_.get_active_player()
    
    def is_leaf(self) -> bool:
        return len(self.children_) == 0
    
    def num_children(self) -> int:
        return len(self.children_)
    
    def policy_score(self) -> float:
        return self.policy_score_
    
    def visits(self) -> int:
        return self.visits_
    
    def state(self) -> BoardState:
        return self.state_
    
    def add_visit(self):
        self.visits_ += 1

    def branches(self) -> List[int]:
        return self.children_.keys()
    
    def average_value(self) -> float:
        return (self.total_value_ + self.value_) / (self.num_descendants_ + 1)

    def child_at(self, move: int) -> Type['SearchNode']:
        if move not in self.children_:
            raise Exception("Board for requested move not found")
        return self.children_[move]
