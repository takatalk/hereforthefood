import sys
from keras.models import model_from_json
import numpy as np
import json
from keras.preprocessing.image import img_to_array, load_img

if __name__ == '__main__':
        test_list = []
        filename = sys.argv[1]
        img = load_img(filename)
        array = img_to_array(img)
        # array = np.expand_dims(array, axis=0)
        # array = array[1,:]
        test_list.append(array)
        test = np.stack(test_list)
        #test = test.reshape(test.shape[0], 301, 301, 3)
        model_file = open('model.json', 'r').readline()
        json_model = json.loads(model_file)
        model = model_from_json(json_model)
        model.load_weights('weights.hdf', by_name=False)
        predictions = model.predict(test, batch_size=1, verbose=0)
        print(predictions)