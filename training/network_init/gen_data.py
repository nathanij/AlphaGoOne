import os
import numpy as np
import sgfmill

from game_summary import GameSummary


root_dir = '/Users/nathanieljames/Desktop/sgf_games'
state_pool = []
iteration = 0
for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith('.sgf'):
            fpath = os.path.join(root, filename)
            with open(fpath) as f:
                data = f.read()
            game_summary = GameSummary(data)
            if game_summary.is_valid():
                state_pool.extend(game_summary.states_as_arrays())
            if len(state_pool) > 500000:
                s = np.concatenate(state_pool)
                spath = os.path.join('/Users/nathanieljames/Desktop/AlphaGoOne/training/data', f'value_network_data_{iteration}.npz')
                np.savez(spath, states = s)
                iteration += 1
                print(f'Starting iteration {iteration}')
if len(state_pool) > 0:
    states = np.concatenate(state_pool)
    save_path = os.path.join('/Users/nathanieljames/Desktop/AlphaGoOne/training/data', f'value_network_data_{iteration}.npz')
    np.savez(save_path, states = states)


