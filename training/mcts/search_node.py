from typing import List, Optional, Tuple, Type
from board_state import BoardState


class SearchNode:
    def __init__(self, parent: Optional[Type['SearchNode']], state: BoardState):
        self.parent_ = parent
        self.state_ = state
        self.visits_ = 0
        self.value_ = 0  # determined by the value network, called when the node is made
        self.policy_score_ = 0
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
