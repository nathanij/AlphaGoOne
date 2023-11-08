import keras
import numpy as np

model_iter = 7
for i in range(27):
    load_path = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/data/value_network_data_{i}.npz'
    data = np.load(load_path)
    training_set = data['states']
    tag_set = data['tags']
    acc_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestAcc{model_iter}'
    loss_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestLoss{model_iter}'
    y_val = tag_set.astype('float32')
    x_val = training_set
    accModel = keras.models.load_model(acc_filepath)
    lossModel = keras.models.load_model(loss_filepath)
    print("Acc. model results:")
    accModel.evaluate(x_val, y_val)
    print("Loss model results:")
    lossModel.evaluate(x_val, y_val)