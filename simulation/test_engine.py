class TestEngine:
    def __init__(self):
        self.valid_ = set(range(362)) # 361 signifying pass

    def reset_valid(self):
        self.valid_ = set(range(362))

    def move(self, board):
        move = self.valid_.pop()
        return move
