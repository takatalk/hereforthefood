import sys
from keras.models import model_from_json
import numpy as np
import json
from keras.preprocessing.image import img_to_array, load_img
import glob


filtered_list = []
nonfiltered_list = []
for filename in glob.glob('home/hackathonuser/instagramDataset/filterValidation_resized/*.jp*g'):
        img = load_img(filename)
        array = img_to_array(img)
        filtered_list.append(array)
for filename in glob.glob('home/hackathonuser/instagramDataset/noFilterValidation_resized/*.jp*g'):
        img = load_img(filename)
        array = img_to_array(img)
        nonfiltered_list.append(array)

# array = np.expand_dims(array, axis=0)
# array = array[1,:]

filtered_test = np.stack(filtered_list)
nonfiltered_test = np.stack(nonfiltered_list)
#test = test.reshape(test.shape[0], 301, 301, 3)
model_file = open('model.json', 'r').readline()
json_model = json.loads(model_file)
model = model_from_json(json_model)
model.load_weights('weights.hdf', by_name=False)
predictions_filtered = model.predict(filtered_test, verbose=0)
print("filtered list: " + predictions_filtered)
predictions_noFiltered = model.predict(nonfiltered_test, verbose=0)
print("nonfiltered list: " + predictions_noFiltered)