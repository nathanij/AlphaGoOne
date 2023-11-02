from sgfmill import boards, sgf_moves, sgf

path = '/Users/nathanieljames/Downloads/F.sgf'
with open(path) as f:
    data = f.read()

game = sgf.Sgf_game.from_string(data)
board, moves = sgf_moves.get_setup_and_moves(game)
# board = boards.Board(19)
def display(board):
    for i in range(19):
        a = ''
        for j in range(19):
            q = board.get(i, j)
            if q is None:
                a += '.'
            else:
                a += q
        print(a)
print(moves)
# print('\n')
# board.play(0,0, 'w')
# board.play(0,1,'b')
# board.play(0,2, 'w')
# board.play(3,3,'b')
# board.play(1,1,'w')
# display(board)
