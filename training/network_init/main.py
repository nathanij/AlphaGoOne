import os
import numpy as np
import sgfmill

from game_summary import GameSummary


root_dir = '/Users/nathanieljames/Desktop/sgf_games'
state_pool = []
count = 0
for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith('.sgf'):
            if count % 100 == 0:
                print(count // 100)
            count += 1
            fpath = os.path.join(root, filename)
            with open(fpath) as f:
                data = f.read()
            game_summary = GameSummary(data)  # TODO
            if game_summary.is_valid():
                state_pool.append(game_summary.states_as_arrays())  # TODO
states = np.concatenate(state_pool)
save_path = os.path.join('data', f'value_network_states.npz')
np.savez(save_path, states = states)


