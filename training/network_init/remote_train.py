import numpy as np
import random
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers


load_path = f'/afs/ece/usr/nathanij/Private/18500/colab_data_50k.npz'
data = np.load(load_path)
training_set = data['states']
tag_set = data['tags']
del data
x_train, x_val, y_train, y_val = train_test_split(training_set, tag_set, test_size=0.2, random_state=19)
del training_set
del tag_set

input_shape = (19, 19, 1)  # Input shape for a 19x19 vector with a single channel
output_dim = 1  # For binary classification
x_train = x_train.reshape(-1, 19, 19, 1)
x_val = x_val.reshape(-1, 19, 19, 1)
training_iter = 0

acc_filepath = f'/afs/ece/usr/nathanij/Private/18500/weights/acc{training_iter}'
loss_filepath = f'/afs/ece/usr/nathanij/Private/18500/weights/loss{training_iter}'
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
    layers.Conv2D(32, (7, 7), activation='relu'),
    layers.Conv2D(64, (7, 7), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(output_dim, activation='sigmoid')
])

schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=10000, decay_rate=0.9)
optimizer = tf.keras.optimizers.Adam(learning_rate=schedule)

model.compile(loss='binary_crossentropy', optimizer = optimizer, metrics=['binary_accuracy'])

model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size = 128, epochs = 1000, shuffle=True, callbacks = [acc_callback, loss_callback, early])