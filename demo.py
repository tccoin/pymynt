
import pymynt
import cv2

pymynt.init_camera()
while True:
    depth = pymynt.get_depth_image()
    left = pymynt.get_left_image()

    if left.size>10:
        cv2.imshow('left', left)
        cv2.waitKey(10)
