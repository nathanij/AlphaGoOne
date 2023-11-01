import numpy as np
from sgfmill import boards, sgf_moves, sgf

def display(board):
    b = [['.'] * 19 for _ in range(19)]
    for row in range(19):
        for col in range(19):
            r = board.get(row, col)
            if r is not None:
                b[row][col] = r
    for row in b:
        print(row)

def flatten(board):
    arr = [0] * 361
    for row in range(19):
        for col in range(19):
            r = board.get(row, col)
            if r is not None:
                stone = -1 if r == 'b' else 1
                arr[19 * row + col] = stone
    return arr
    



class GameSummary:
    def __init__(self, data: str):
        self.game_ = sgf.Sgf_game.from_string(data)
        self.winner_ = None
        try:
            self.winner_ = self.game_.get_winner()
        except:
            self.winner_ = None
            return
        try:
            if self.game_.get_size() != 19:
                self.winner_ = None
                return
        except:
            self.winner_ = None
            return
        self.states_ = None
        if self.winner_ is None or (self.winner_ != 'b' and self.winner_ != 'w'):
            return
        self.winner_ = 0 if self.winner_ == 'b' else 1
        board = boards.Board(19)
        self.states_ = []
        _, moves = sgf_moves.get_setup_and_moves(self.game_)
        turn = 0
        state = flatten(board)
        state.append(turn)
        state.append(self.winner_)
        self.states_.append(np.asarray(state))
        for color, coords in moves:
            try:
                y, x = coords
                board.play(y, x, color)
            except:
                self.winner_ = None
                return
            state = flatten(board)
            state.append(turn)
            state.append(self.winner_)
            self.states_.append(np.asarray(state))
    
    def is_valid(self):
        return self.winner_ is not None

    def states_as_arrays(self):
        return self.states_
            