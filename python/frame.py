import cv2
import numpy as np
img=np.zeros((300,400),dtype=np.uint8)
img[0:50,:]=0
img[50:100,:]=50
img[100:150,:]=100
img[150:200,:]=150
img[200:250,:]=200
img[250:300,:]=255

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()