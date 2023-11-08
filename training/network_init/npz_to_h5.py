import numpy as np
import h5py


path = "/Users/nathanieljames/Desktop/AlphaGoOne/training/data/colab_data_75k.npz"
data = np.load(path)
training_set = data['states']
tag_set = data['tags']
path = "/Users/nathanieljames/Desktop/AlphaGoOne/training/data/colab_data_75k.npz"


with h5py.File("/Users/nathanieljames/Desktop/AlphaGoOne/training/data/50ktrain.h5", "w") as file:
    # Create datasets and store the NumPy arrays
    file.create_dataset("states", data=training_set)
    file.create_dataset("tags", data=tag_set)