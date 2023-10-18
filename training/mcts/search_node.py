from typing import List, Optional, Tuple, Type
from board_state import BoardState


class SearchNode:
    def __init__(self, parent: Optional[Type['SearchNode']], state: BoardState):
        self.parent_ = parent
        self.state_ = state
        self.visits_ = 0
        self.eval_ = 0
        self.total_value_ = 0  # cumulative value score (not divided by visits)
        # initial value will be the value networks eval, supplied by driver
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
    
    def average_value(self):
        pass

    def child_at(self, move: int) -> Tuple[float, Type['SearchNode']]:  # TODO: check if this typing is correct
        if move not in self.children_:
            raise Exception("Board for requested move not found")
        return self.children_[move]
