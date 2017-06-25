import sys
from keras.models import model_from_json
from skimage.novice import open as sci_open
import json

if __name__ == '__main__':
	filename = sys.argv[1]
	array = sci_open(filename).array
	test = [array]
	model_file = open('model.json', 'r').readline()
	json_model = json.loads(model_file)
	json_model = json.loads(json_model)
	model = model_from_json(json_model)
	model.load_weights('weights.hdf', by_name=False)
	model.predict(test, batch_size=1, verbose=0)
