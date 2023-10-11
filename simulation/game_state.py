class GameState:
    def __init__(self, size = 19):
        self.size_ = size
        self.board_ = [[0] * size for _ in range(size)] # -1 for black, 1 for white
        self.prev_states_ = set()

    def finished(self):
        pass

    def make_move(self, move):
        
