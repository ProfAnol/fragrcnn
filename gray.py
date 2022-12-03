import cv2
import numpy as np
#读取图片
image = cv2.imread("D:\\MASKRCNN\\images\\test2.jpg")     
cv2.imshow('original',image)

#灰度处理
im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',im_gray)

cv2.waitKey()
cv2.destroyAllWindows()