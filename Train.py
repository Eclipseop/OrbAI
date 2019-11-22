import pickle
import os
import random
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import cv2

ANSWERS = ['R', 'G', 'B', 'L', 'D', 'H', 'J']

def generate_model():
    data = os.listdir("data")
    random.shuffle(data)

    training_data = []
    training_answer = []
    for file in data:
        training_data.append(cv2.imread('data/' + file, cv2.IMREAD_GRAYSCALE))
        training_answer.append(ANSWERS.index(file[0]))

    training_data = np.array(training_data)
    nsamples, nx, ny = training_data.shape
    training_data = training_data.reshape((nsamples,nx*ny))

    training_data, testing_data = np.array_split(training_data, 2)
    training_answer, testing_answer = np.array_split(training_answer, 2)

    clf = KNeighborsClassifier()
    clf.fit(training_data, training_answer)
    print('Score: ', clf.score(testing_data, testing_answer))

    pickle.dump(clf, open('model.pickle', 'wb'))
    return clf

if __name__ == "__main__":
    generate_model()
