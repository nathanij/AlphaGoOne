import os
import numpy as np
import random
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
                random.shuffle(state_pool)
                states = []
                tags = []
                for state, tag in state_pool:
                    states.append(state)
                    tags.append(tag)
                s = np.stack(states)
                spath = os.path.join('/Users/nathanieljames/Desktop/AlphaGoOne/training/data', f'value_network_data_{iteration}.npz')
                np.savez(spath, states = s, tags = np.asarray(tags))
                print(f'Ending length: {len(state_pool)}')
                state_pool = []
                iteration += 1
                print(f'Starting iteration {iteration}')
if len(state_pool) > 0:
    random.shuffle(state_pool)
    states = []
    tags = []
    for state, tag in state_pool:
        states.append(state)
        tags.append(tag)
    s = np.vstack(states)
    spath = os.path.join('/Users/nathanieljames/Desktop/AlphaGoOne/training/data', f'value_network_data_{iteration}.npz')
    np.savez(spath, states = s, tags = np.asarray(tags))
    print(f'Ending length: {len(state_pool)}')


