import cv2
import numpy as np

cap = cv2.VideoCapture('videos/Transport.mp4')

while True:
    success, img = cap.read()

    #img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    img = cv2.GaussianBlur(img, (9, 9), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.Canny(img, 30, 30)

    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.erode(img, kernel, iterations=1)

    # img[0:200, 0:350]
    cv2.imshow('Result', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# print(img.shape)

cv2.waitKey(0)