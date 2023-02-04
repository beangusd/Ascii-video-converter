import cv2
import os

vid = cv2.VideoCapture("file path")

try:

    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('oopsies')

currentframe = 0

while (True):

    success, frame = vid.read()

    if success:
        name = './data/frame' + str(currentframe) + '.jpg'
        print('yay it works')
        cv2.imwrite(name, frame)
    else:
        break
vid.release()
cv2.destroyAllWindows()
