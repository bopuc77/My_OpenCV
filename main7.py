import cv2
import numpy


photo = cv2.imread('images\my_images.jpg')
img = numpy.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (1500, 155), (950, 950), 255, -1)


img = cv2.bitwise_and(photo, photo, mask=square)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(square)


cv2.imshow('Result', img)
cv2.waitKey(0)