'''Train a simple deep CNN on the CIFAR10 small images dataset.

GPU run command with Theano backend (with TensorFlow, the GPU is automatically used):
    THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatx=float32 python cifar10_cnn.py

It gets down to 0.65 test logloss in 25 epochs, and down to 0.55 after 50 epochs.
(it's still underfitting at that point, though).
'''

from __future__ import absolute_import, print_function
# from ..utils.data_utils import get_file
# from .. import backend as K
import sys
import os
import numpy as np
import glob
from six.moves import cPickle
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import img_to_array, load_img
# from matplotlib import pyplot as plt
import load
import json

#------------------------------------------------------------------

# def load_data(label_mode='fine'):
#     """Loads CIFAR100 dataset.

#     # Arguments
#         label_mode: one of "fine", "coarse".

#     # Returns
#         Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

#     # Raises
#         ValueError: in case of invalid `label_mode`.
#     """
#     if label_mode not in ['fine', 'coarse']:
#         raise ValueError('label_mode must be one of "fine" "coarse".')

#     dirname = 'cifar-100-python'
#     origin = 'http://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz'
#     path = get_file(dirname, origin=origin, untar=True)

#     fpath = os.path.join(path, 'train')
#     x_train, y_train = load_batch(fpath, label_key=label_mode + '_labels')

#     fpath = os.path.join(path, 'test')
#     x_test, y_test = load_batch(fpath, label_key=label_mode + '_labels')

#     y_train = np.reshape(y_train, (len(y_train), 1))
#     y_test = np.reshape(y_test, (len(y_test), 1))

#     if K.image_data_format() == 'channels_last':
#         x_train = x_train.transpose(0, 2, 3, 1)
#         x_test = x_test.transpose(0, 2, 3, 1)

#     return (x_train, y_train), (x_test, y_test)


#------------------------------------------------------------------

# train_set, test_set = load.load_imgs()

#------------------------------------------------------------------

batch_size = 100
num_classes = 2
epochs = 20
data_augmentation = True

# The data, shuffled and split between train and test sets:
(x_train, y_train), (x_test, y_test) = load.load_imgs() #cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# initiate RMSprop optimizer
opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

# Let's train the model using RMSprop
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

if not data_augmentation:
    print('Not using data augmentation.')
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(x_test, y_test),
              shuffle=True)
else:
    print('Using real-time data augmentation.')
    # This will do preprocessing and realtime data augmentation:
    datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=0,  # randomly rotate images in the range (degrees, 0 to 180)
        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=True,  # randomly flip images
        vertical_flip=False)  # randomly flip images

    # Compute quantities required for feature-wise normalization
    # (std, mean, and principal components if ZCA whitening is applied).
    datagen.fit(x_train)

    # Fit the model on the batches generated by datagen.flow().
    model.fit_generator(datagen.flow(x_train, y_train,
                                     batch_size=batch_size),
                        steps_per_epoch=x_train.shape[0] // batch_size,
                        epochs=epochs,
                        validation_data=(x_test, y_test))

    json_data = model.to_json()
    with open('model.json', 'w') as outfile:
    json.dump(json_data, outfile)
    model.save_weights('weights.hdf')
