import sys
from keras.models import model_from_json
from skimage.novice import open as sci_open


if __name__ == '__main__':
	filename = sys.argv[1]
	array = sci_open(filename).array
	test = [array]
	print(test)
	json = open('model.json', 'r')
	model = model_from_json(json)
	model.load_weights('weights.hdf', by_name=False)
	model.predict(test, batch_size=1, verbose=0)
