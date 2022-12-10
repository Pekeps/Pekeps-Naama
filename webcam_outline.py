import cv2
import numpy as np
import time as t

gscale2 = "@%#*+=-:. "         #10 levels of gray
# Setup webcam camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 0)
    gb = cv2.GaussianBlur(frame, (5, 5), 0)
    can = cv2.Canny(gb, 127, 31)
    cv2.imshow('Canny edge detection', can)
    cv2.imshow("Webcam", gb)


    if cv2.waitKey(1) == 32:
        timestr = t.strftime("%Y%m%d-%H%M%S")
        cv2.imwrite("frame%s.jpg" % timestr, can)








    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

def generate_ascii_letters():
    images = []
    #letters = "# $%&\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    letters = " \\ '(),-./:;[]_`{|}~"
    for letter in letters:
        img = np.zeros((12, 16), np.uint8)
        img = cv2.putText(img, letter, (0, 11), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
        images.append(img)
    return np.stack(images)