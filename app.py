import pickle
import numpy as np
import pyautogui
import cv2
import train

ANSWERS = ['R', 'G', 'B', 'L', 'D', 'H', 'J']


def get_model():
    model = None
    try:
        model = pickle.load(open('model.pickle', 'rb'))
    except FileNotFoundError:
        print('Model not found, creating a new one...')
        model = train.generate_model()

    return model


def get_orb_images():
    images = []

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

            orb_image = image[y:dy, x:dx]
            orb_image = cv2.cvtColor(orb_image, cv2.COLOR_BGR2GRAY)
            orb_image = np.array(orb_image)
            mnx, mny = orb_image.shape
            orb_image = orb_image.reshape((mnx*mny))
            images.append(orb_image)

    return images


def generate_board_string():
    board_string = ""
    for image in get_orb_images():
        board_string += ANSWERS[get_model().predict([image])[0]]
    return board_string


def debug_window():
    image = pyautogui.screenshot()
    image = np.array(image)
    x = 733
    y = 588
    h = 377
    w = 452
    image = image[:, :, ::-1].copy()
    image = image[y:y+h, x:x+w]

    board_string = generate_board_string()
    for row in range(0, 5):
        for column in range(0, 6):
            x = (76 * column) - column
            y = (76 * row) - row
            dx = x + 75
            dy = y + 75

            prediction = board_string[row * 6 + column]
            image = cv2.putText(image, prediction, (x + 38, y + 38),
                                cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 0))
            image = cv2.putText(image, prediction, (x + 37, y + 37),
                                cv2.FONT_HERSHEY_PLAIN, 1.2, (row * 40, column * 40, 255))
            image = cv2.rectangle(image, (x, y), (dx, dy), (255, 255, 255), 1)

    cv2.imshow("Screenshot", image)
    cv2.waitKey(100)


if __name__ == "__main__":
    while True:
        debug_window()
