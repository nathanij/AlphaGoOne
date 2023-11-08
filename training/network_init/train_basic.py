import numpy as np
import tensorflow as tf
import keras
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers
import absl.logging
import random

# TODO: change to one hot encoding (0 for black, 1 for white, 0.5 for empty)

absl.logging.set_verbosity(absl.logging.ERROR)

# TODO: try loading full data set at once and training on it overnight

training_iter = 9
tset = []
tags = []
sector_length = 5000 # 75000
for i in range(27): # 27
    print(i)
    load_path = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/data/value_network_data_{i}.npz'
    data = np.load(load_path)
    tset.append(data['states'][:sector_length])
    tags.append(data['tags'][:sector_length])
    del data

training_set = np.concatenate(tset)
del tset
tag_set = np.concatenate(tags).astype('float32')
del tags

print('here')

x_train, x_val, y_train, y_val = train_test_split(training_set, tag_set, test_size=0.2, random_state=20)
del training_set
del tag_set

input_shape = (19, 19, 1)  # Input shape for a 19x19 vector with a single channel
output_dim = 1  # For binary classification

# y_val = tag_set[:validation_size]
# y_train = tag_set[validation_size:]
# x_val = training_set[:validation_size]
# x_train = training_set[validation_size:]
print(x_train.shape)
print(x_val.shape)
x_train = x_train.reshape(-1, 19, 19, 1)
x_val = x_val.reshape(-1, 19, 19, 1)

acc_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestAcc{training_iter}'
loss_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestLoss{training_iter}'
acc_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=acc_filepath,
    save_weights_only=False,
    monitor='val_binary_accuracy',
    mode='max',
    save_best_only=True)
loss_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=loss_filepath,
    save_weights_only=False,
    monitor='val_loss',
    mode='min',
    save_best_only=True)
early = tf.keras.callbacks.EarlyStopping(monitor="val_loss",patience = 20)

input_shape = (19, 19, 1)
model = tf.keras.Sequential([
    layers.Input(shape=input_shape),
    layers.Conv2D(128, (3, 3), activation='relu', padding = 'same'),
    layers.Conv2D(64, (5,5), activation='relu', padding = 'same'),
    layers.Conv2D(32, (7, 7), activation='relu', padding = 'same'),
    layers.Conv2D(16, (9,9), activation='relu', padding = 'same'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(16, activation='relu'),
    layers.Dense(output_dim, activation='sigmoid')
])

schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=10000, decay_rate=0.9)
optimizer = tf.keras.optimizers.Adam(learning_rate=schedule)

model.compile(loss='binary_crossentropy', optimizer = optimizer, metrics=['binary_accuracy'])

# Reshape your input data to match the input shape

model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size = 128, epochs = 1000, shuffle=True, callbacks = [acc_callback, loss_callback, early])

