import cv2
import os
import glob

for file in glob.glob("*.jpg"):
    img = cv2.imread(file,1)
    resized_img = cv2.resize(img, (100,100))
    cv2.imshow("resized_"+file,resized_img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" +file, resized_img)
