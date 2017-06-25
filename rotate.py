from skimage import data
from skimage.transform import rotate
from skimage.novice import open
import scipy.misc
import numpy as np
import glob
import os

def getMoreImgs(imgArray):
	imgs = []
	imgs.append(imgArray)
	imgs.append(np.rot90(imgs[-1]))
	imgs.append(np.rot90(imgs[-1]))
	imgs.append(np.rot90(imgs[-1]))
	imgs.append(np.fliplr(imgArray))
	imgs.append(np.flipud(imgArray))
	imgs.append(np.fliplr(imgs[-1]))
	return imgs

B = ['b', 'c', 'd' ,'e', 'f', 'g', 'i']
a = 0
for filename in glob.glob('newdata/false/*.jpg'): #for filename in glob.glob('data/false/*.jpeg'):
	img = open(filename)
	array = getMoreImgs(img.array)
	b = 0
	for i in array:
		scipy.misc.imsave('false/{}{}.jpg'.format(str(a).zfill(3), B[b]), i)
		b += 1
	a += 1