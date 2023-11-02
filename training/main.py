import os
import numpy as np
from sim_driver import SimDriver

run_iter = 0  # increment with each run to distinguish data

weight_path = os.path.join('networks', 'weights')
policy_network_path = os.path.join(weight_path, 'policy.pt')
value_network_path = os.path.join(weight_path, 'value.pt')

input_arrays = []       # board state + turn
value_tag_arrays = []   # game result
policy_tag_arrays = []  # Normalized MCTS visit counts

exploration_factor = 1  # TODO: research what a reasonable value for this is, and how it shifts
search_limit = 100  # starting very low
expansion_limit = 362  # up to how many legal moves generated during MCTS, can decrease as policy network strength increases
sim_driver = SimDriver(policy_network_path, value_network_path, 
                       exploration_factor, search_limit, expansion_limit)
sim_length = 2  # TODO: change to much larger once tested
for _ in range(sim_length):
    sim_driver.simulate()
    input_arrays.append(sim_driver.training_states())
    value_tag_arrays.append(sim_driver.result_tags())
    policy_tag_arrays.append(sim_driver.policy_tags())

input_data = np.concatenate(input_arrays) # TODO: check vstack and concat here
value_tags = np.concatenate(value_tag_arrays)
policy_tags = np.concatenate(policy_tag_arrays)

save_path = os.path.join('data', f'training_data_{run_iter}.npz')
np.savez(save_path, input_data = input_data, value_tags = value_tags,
         policy_tags = policy_tags)
