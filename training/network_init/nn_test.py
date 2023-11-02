import keras
import numpy as np

training_iter = 0
load_path = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/data/value_network_data_{training_iter}.npz'
data = np.load(load_path)
training_set = data['states']
tag_set = data['tags']
validation_size = 75000
acc_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestAcc{training_iter}'
loss_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestLoss{training_iter}'

y_val = tag_set[:validation_size].astype('float32')
y_train = tag_set[validation_size:].astype('float32')
x_val = training_set[:validation_size]
x_train = training_set[validation_size:]
print(training_set.shape)


accModel = keras.models.load_model(acc_filepath)
lossModel = keras.models.load_model(loss_filepath)


accModel.evaluate(x_val, y_val)

lossModel.evaluate(x_val, y_val)