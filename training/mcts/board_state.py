from copy import deepcopy
import random
from typing import List

class BoardState:
    def __init__(self, size = 19):
        self.size_ = size
        self.board_ = [[0] * size for _ in range(size)] # -1 for black, 1 for white
        row, col = random.randint(0, 18), random.randint(0, 18) # TODO: should I randomize here, or just iterate all 361 possibilities, then retrain
        # TODO: enquire about randmoziing beyond just the first move
        self.board_[row][col] = 1  # randomized first move
        self.prev_states_ = set()
        self.active_ = 1 # white moves post-randomization
        self.pass_count_ = 0

    def finished(self) -> bool:
        return self.pass_count_ == 2
    
    def get_flattened_state(self) -> List[int]:
        flat_state = []
        for row in self.board_:
            flat_state += row
        return flat_state
    
    def get_active_player(self) -> bool:
        return self.active_
    
    def bfs_(self, row, col, visited, prevs, match_color) -> bool:
        if row < 0 or col < 0 or row >= self.size_ or col >= self.size_:
            return False
        coord = (row, col)
        if coord in prevs or coord in visited:
            return False
        
        if self.board_[row][col] == 0:
            return True # unrestricted edge
        if self.board_[row][col] == -match_color:
            return False # restricted edge
        prevs.add(coord)

        
        # implicitly board[row][col] = opposing color
        adj = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        retval = False
        for y,x in adj:
            retval = retval or self.bfs_(y, x, visited, prevs, match_color)
        return retval
    
    # repeat BFS for moving player to check liberties if no captures are made


    def validate_move_(self, row, col) -> bool:
        # check if space is already occupied
        if self.board_[row][col] != 0:
            return False
        
        # set up for bfs
        move_color = 1 if self.active_ else -1
        visited = set()
        captured = []
        self.board_[row][col] = move_color

        # bfs through adjacent points
        foci = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for y, x in foci:
            prevs = set()
            if not self.bfs_(y, x, visited, prevs, -move_color):
                for point in prevs:
                    captured.append(point)
            visited.union(prevs)

        # if no captures check if placement has liberties
        if len(captured) == 0:
            if not self.bfs_(row, col, set(), set(), move_color):
                self.board_[row][col] = 0
                return False

        # make captures
        self.board_[row][col] = move_color
        for y, x in captured:
            self.board_[y][x] = 0

        # check for repeated board state
        updated_board = tuple(tuple(row) for row in self.board_)
        if updated_board in self.prev_states_:
            for y, x in captured:
                self.board_[y][x] = -move_color
            self.board_[row][col] = 0
            return False
        self.prev_states_.add(updated_board)
        return True

    def make_move(self, move) -> bool:
        if move == self.size_ ** 2:
            self.pass_count_ += 1
            return True
        row = move // self.size_
        col = move % self.size_
        if not self.validate_move_(row, col):
            return False
        self.pass_count_ = 0
        self.active_ = not self.active_
        return True
