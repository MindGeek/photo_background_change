from __future__ import print_function
import sys
import cv2
import numpy as np


def pixel_like(a, b, value=20):
    a = a.copy()
    a = np.array([a[0]*10, a[1]*10, a[2]])
    b = b.copy()
    b = np.array([b[0]*10, b[1]*10, b[2]])
    dist = np.sqrt(np.sum(np.square(a - b)))
    return dist < value


img_file = sys.argv[1]
img = cv2.imread(sys.argv[1])
img_old = img.copy()
X, Y, C = np.shape(img)

# get background color
tar = img[30, 30].copy()

for x in range(X):
    for y in range(Y):
        if pixel_like(img[x, y], tar, int(sys.argv[2])):
            img[x, y] = np.array([255, 255, 255])

cv2.imshow('img old', img_old)
img = cv2.resize(img, dsize=(0, 0), fx=2.1, fy=2.1)
cv2.imshow('img update', img)
cv2.waitKey(0)
cv2.imwrite(img_file + '.new.jpg', img)

#img_eroded = cv2.erode(img, cv2.getStructuringElement(cv2.MORPH_CROSS, (1, 1)), iterations=1)
#cv2.imshow('img eroded', img_eroded)

