from mcts.search_tree_header import SearchTreeHeader


class SearchDriver:
    # Minimize instead of maximize if black is moving
    def __init__(self, tree: SearchTreeHeader, search_limit: int, active_player: int):
        self.tree_ = tree
        self.active_player_ = active_player
        self.iterations_ = 0
        self.search_limit_ = search_limit

    def finished(self):
        return self.iterations_ >= self.search_limit_
    