import os
import numpy as np
import h5py


tset = []
tags = []
sector_length = 50000 # 75000
for i in range(27): # 27
    print(i)
    load_path = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/data/value_network_data_{i}.npz'
    data = np.load(load_path)
    tset.append(data['states'][:sector_length])
    tags.append(data['tags'][:sector_length])
    del data

tset = np.concatenate(tset)
tags = np.concatenate(tags).astype('float32')

with h5py.File("/Users/nathanieljames/Desktop/AlphaGoOne/training/data/50ktrain_2.h5", "w") as file:
    # Create datasets and store the NumPy arrays
    file.create_dataset("states", data=tset)
    file.create_dataset("tags", data=tags)