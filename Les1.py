import cv2 as cv # importing openCV and giving it variable name cv
import sys       # importing system commands
import numpy

#cv.samples.addSamplesDataSearchPath("/home/pi/opencv/samples/data")
#img = cv.imread(cv.samples.findFile("squares.jpg"))
img = cv.imread(cv.samples.findFile("starry_night.jpg"))

if img is None:
    sys.exit("Could not read the image")

cv.imshow("Display window", img)
k = cv.waitKey(200)

if k == ord("s"):
    cv.imwrite("squares.png", img)
