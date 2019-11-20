import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import cv2
import os
import random
import pyautogui
import time

ANSWERS = ['R', 'G', 'B', 'L', 'D', 'H', 'J']

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

while True:
    image = pyautogui.screenshot()
    image = np.array(image)
    x = 733
    y = 588
    h = 377
    w = 452
    image = image[:, :, ::-1].copy()
    image = image[y:y+h, x:x+w]
    
    for row in range(0, 5):
        for column in range(0, 6):
            x = (76 * column) - column
            y = (76 * row) - row
            dx = x + 75
            dy = y + 75
            
            test_image = image[y:dy, x:dx]
            test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
            test_image = np.array(test_image)
            mnx, mny = test_image.shape
            test_image = test_image.reshape((mnx*mny))
            
            prediction = ANSWERS[clf.predict([test_image])[0]]
            image = cv2.putText(image, prediction, (x + 38,y + 38), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 0))
            image = cv2.putText(image, prediction, (x + 37,y + 37), cv2.FONT_HERSHEY_PLAIN, 1.2, (row * 40, column * 40, 255))
            image = cv2.rectangle(image, (x, y), (dx, dy), (255, 255, 255), 1)
    
    
    cv2.imshow("Screenshot", image)
    cv2.waitKey(1)
