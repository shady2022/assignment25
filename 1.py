import cv2
import numpy as np

image = cv2.imread("C:\\python_programming\\tamrin5\\1\\flower_input.jpg")

bblr11 = cv2.bilateralFilter(image, 11, 110, 110)

bblur = np.vstack([np.hstack ([image, bblr11])])

cv2.imshow("result1.jpg", bblr11)
cv2.waitKey()
cv2.destroyAllWindows()