from typing import List, Optional, Type


class SearchNode:
    def __init__(self, parent: Optional[Type['SearchNode']], state: List[List[int]]):
        self.parent_ = parent
        self.state_ = state
        self.children_ = []

    def 
