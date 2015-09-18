#!/usr/bin/python
from freenect import sync_get_depth
import cv  
import cv2
import frame_convert

cv.NamedWindow('Depth')

def get_depth():
    img=frame_convert.pretty_depth_cv(sync_get_depth()[0])
    return img

while 1:
    cv.ShowImage('Depth', get_depth())
    if cv.WaitKey(10) == 27:
        break
