from training.mcts import search_tree_header


class SearchDriver:
    def __init__(self, tree: search_tree_header):
        self.tree_ = tree
        