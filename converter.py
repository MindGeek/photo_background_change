from __future__ import print_function
import sys
import cv2
import numpy as np


def pixel_like(a, b, value=300):
    """ When deal with 'blue' background,
    you must ignore the other chanel to make it easier to find out all the 'blue like' point """
    a = np.array([a[0]*10, a[1]*10, a[2]])
    b = np.array([b[0]*10, b[1]*10, b[2]])
    dist = np.sqrt(np.sum(np.square(a - b)))
    return dist < value


def convert(img_file, img_file_new):
    img = cv2.imread(img_file)
    img_old = img.copy()
    X, Y, C = np.shape(img)

    # get background color
    tar = img[30, 30].copy()

    for x in range(X):
        for y in range(Y):
            if pixel_like(img[x, y], tar):
                img[x, y] = np.array([255, 255, 255])

    #cv2.imshow('img old', img_old)  # for debug
    #img = cv2.resize(img, dsize=(0, 0), fx=2.1, fy=2.1)  # for my own use
    #cv2.imshow('img update', img)  # for debug
    #cv2.waitKey(0)
    cv2.imwrite(img_file_new, img)


if __name__ == '__main__':
    img_file = sys.argv[1]
    img_file_new = img_file + '.new.jpg'
    convert(img_file, img_file_new)
