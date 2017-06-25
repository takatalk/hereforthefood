from PIL import Image
import numpy as np
import glob
import os

resizedFolderName = "instagramDataSet/notFiltered_resized"
for filename in glob.glob('instagramDataSet/notFiltered/*.jp*g'): #for filename in glob.glob('data/false/*.jpeg'):
    filenameOnly, file_extension = os.path.splitext(filename)
    image=Image.open(filename)
    resizedImage = image.resize((301,301))
    head, tail = os.path.split(filenameOnly)
    relativePath = "./" + resizedFolderName + "/" + tail + "_resized.jpg"
    resizedImage.save(relativePath)