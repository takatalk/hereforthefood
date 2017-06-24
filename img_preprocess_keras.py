import numpy as np
np.random.seed(123)
import glob
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D

from keras.utils import np_utils
from keras.preprocessing.image import array_to_img, img_to_array, load_img

from matplotlib import pyplot as plt

# load data
x_train = []
y_train = []

# Loading in real, unedited images
for filename in glob.glob('data/true/*.jpeg'): #for filename in glob.glob('data/false/*.jpeg'):
    img = load_img(filename)
    imgArray = img_to_array(img)
    imgArray = imgArray.reshape((1,) + imgArray.shape)
    print(imgArray.shape)
    print(imgArray)
    x_train.append(imgArray)
    y_train.append(1)

# Loading in edited images
for filename in glob.glob('data/false/*.jpeg'):
    img = load_img(filename)
    imgArray = img_to_array(img)
    # imgArray = imgArray.reshape(1, 3, 301, 301)
    x_train.append(imgArray)
    y_train.append(0)

print(y_train)