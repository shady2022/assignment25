import numpy as np
import cv2

img = cv2.imread('C:\python_programming\tamrin5\1\flower_input.jpg')


result = np.zeros(img.shape)
mask = np.ones((25,25)) / 225
rows , cols = img.shape

for i in range (12,rows-12):
    for j in range(12,cols-12):
        if img[i, j]< 120:
                small_img = img[i-12:i+13, j-12:j+13]
                result[i, j] = np.sum(small_img * mask)
        else:
            result[i, j] = img[i, j]
          

cv2.imshow('blurred background' , img)                  
cv2.imwrite("output.jpg", img)
cv2.waitKey()