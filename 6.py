import cv2
import numpy as np


def filter(img, value):
    img = cv2.imread('C:\\python_programming\\tamrin5\\5\\myface.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    res = filter(img, 15)
    mask = np.ones((value, value))/(value** 2)
    result = np.zeros(img.shape)

    rows, cols = img.shape
    for i in range(value//2, rows - value//2):
            for j in range(value//2, cols - value//2):
               small_img = img[i-value//2:i+value//2+1, j-value//2:j+value//2+1]
               result[i, j] = np.sum(small_img * mask)

    return result

img = cv2.imread("myface.jpg")
res = filter(img, 15)
cv2.imwrite('result_4_15x15.jpg', res)
   
