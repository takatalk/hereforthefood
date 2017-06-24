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

def load_imgs():
    # load data
    x_train = []
    y_train = []
    x_test = []
    y_test = []

    x = 0
    # Loading in real, unedited images
    for filename in glob.glob('data/true/*.jpeg'): #for filename in glob.glob('data/false/*.jpeg'):
        img = load_img(filename)
        imgArray = img_to_array(img)
        # imgArray = imgArray.reshape((1,) + imgArray.shape)
        x_train.append(imgArray)
        y_train.append(1)

    y = 0
    # Loading in edited images
    for filename in glob.glob('data/false/*.jpeg'):
        img = load_img(filename)
        imgArray = img_to_array(img)
        # imgArray = imgArray.reshape(1, 3, 301, 301)
        x_train.append(imgArray)
        y_train.append(0)

    y_train = np_utils.to_categorical(y_train, 2)
    return x_train, y_train #(x_train, y_train), (x_test, y_test)