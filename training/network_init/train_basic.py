import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras import layers


training_iter = 0
load_path = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/data/value_network_data_{training_iter}.npz'
data = np.load(load_path)
training_set = data['states']
tag_set = data['tags']

input_shape = (19, 19, 1)  # Input shape for a 19x19 vector with a single channel
output_dim = 1  # For binary classification
validation_size = 75000

y_val = tag_set[:validation_size].astype('float32')
y_train = tag_set[validation_size:].astype('float32')
x_val = training_set[:validation_size]
x_train = training_set[validation_size:]
print(training_set.shape)

acc_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestAcc{training_iter}'
loss_filepath = f'/Users/nathanieljames/Desktop/AlphaGoOne/training/networks/weights/bestLoss{training_iter}'
acc_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=acc_filepath,
    save_weights_only=False,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)
loss_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=loss_filepath,
    save_weights_only=False,
    monitor='val_loss',
    mode='min',
    save_best_only=True)
early = tf.keras.callbacks.EarlyStopping(monitor="val_loss",patience=20)

model = tf.keras.Sequential([
    layers.Input(shape=input_shape),  # Specify the input shape
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(output_dim, activation='sigmoid')  # Output layer for binary classification
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Reshape your input data to match the input shape
x_train = x_train.reshape(-1, 19, 19, 1)
x_val = x_val.reshape(-1, 19, 19, 1)

model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size = 128, epochs = 1000, shuffle=True, callbacks = [acc_callback, loss_callback, early])
