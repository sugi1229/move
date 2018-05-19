import os
import cv2

movie = './test.avi'

count = 0
cap = cv2.VideoCapture(movie)

while True:
    ret, frame = cap.read()
    if ret == True:
        count += 1
        cv2.imwrite('./' + 'test_' + str("{0:05d}".format(count)) +'.jpg', frame)
    else:
        break
