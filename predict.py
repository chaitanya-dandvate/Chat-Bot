from sklearn.externals import joblib
import numpy as np

def process_query(input_query):
	cv = joblib.load('train_vectors.pkl')
	X_cv_test = cv.transform([input_query]).toarray()
	random_forest = joblib.load('train_weights.pkl')
	predictions = random_forest.predict(X_cv_test)
	labels = list(np.load('labels.npy'))
	y = list(np.load('y.npy'))

	for index, i in enumerate(y):
		if i == int(predictions[0]):
			return str(labels[index])
