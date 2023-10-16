import os
import numpy as np
from sim_driver import SimDriver

run_iter = 0

weight_path = os.path.join('networks', 'weights')
policy_network_path = os.path.join(weight_path, 'policy')  # TODO: add file extension once known
value_network_path = os.path.join(weight_path, 'value')

input_arrays = []       # board state + turn
value_tag_arrays = []   # game result
policy_tag_arrays = []  # Normalized MCTS visit counts

sim_driver = SimDriver(policy_network_path, value_network_path)
sim_length = 2  # TODO: change to much larger once tested
for _ in range(sim_length):
    sim_driver.simulate()
    input_arrays.append(sim_driver.training_states())
    value_tag_arrays.append(sim_driver.result_tags())
    policy_tag_arrays.append(sim_driver.policy_tags())

input_data = np.concatenate(input_arrays)
value_tags = np.concatenate(value_tag_arrays)
policy_tags = np.concatenate(policy_tag_arrays)

save_path = os.path.join('data', f'training_data_{run_iter}.npz')
np.savez(save_path, input_data = input_data, value_tags = value_tags,
         policy_tags = policy_tags)
