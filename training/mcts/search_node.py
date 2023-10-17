from typing import Optional, Type
from board_state import BoardState


class SearchNode:
    def __init__(self, parent: Optional[Type['SearchNode']], state: BoardState):
        self.parent_ = parent
        self.state_ = state
        self.visits_ = 0
        self.total_value_ = 0  # cumulative value score (not divided by visits)
        # initial value will be the value networks eval, supplied by driver
        self.children_ = dict()

    def finished(self):
        return self.state_.finished()
    
    def get_flattened_state(self):
        return self.state_.get_flattened_state()
    
    def get_active_player(self):
        return self.state_.get_active_player()

    def child_at(self, move: int) -> Type['SearchNode']:
        if move not in self.children_:
            raise Exception("Board for requested move not found")
        self.children_[move].parent_ = None
        return self.children_[move]

