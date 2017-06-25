from PIL import Image
from PIL import ImageFilter
import numpy as np
import glob

idx = 1001

for filename in glob.glob('~/CameraDataset/JPEGImages/*.jp*g'):
    img = Image.open(filename)
    randNum = np.random.rand()*10
    if(randNum > 0 & randNum < 1):
        img = img.filter(ImageFilter.BLUR)
    elif(randNum >= 1 & randNum < 2):
        img = img.filter(ImageFilter.CONTOUR)
    elif(randNum >= 2 & randNum < 3):
        img = img.filter(ImageFilter.DETAIL)
    elif(randNum >= 3 & randNum < 4):
        img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif(randNum >= 4 & randNum < 5):
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif(randNum >= 5 & randNum < 6):
        img = img.filter(ImageFilter.FIND_EDGES)
    elif(randNum >= 6 & randNum < 7):
        img = img.filter(ImageFilter.SMOOTH)
    elif(randNum >= 7 & randNum < 8):
        img = img.filter(ImageFilter.SMOOTH_MORE)
    elif(randNum >= 8 & randNum < 9):
        img = img.filter(ImageFilter.SHARPEN)
    img.save('~/CameraDataset/altered/%s' % str(idx), 'JPEG')
    idx +=1