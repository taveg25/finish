#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from trace import trace

@trace
def initialize():
    cap = cv2.VideoCapture(0)
    qrDecoder = cv2.QRCodeDetector()
    return cap, qrDecoder


@trace
def finalize(cap):
    cap.release()
    cv2.destroyAllWindows()
    
def frame_box(box, image):
    n = len(box)
    for k in range(0,n):
        a = tuple(box[k][0])
        if k+1>=n:
            b = tuple(box[0][0])
        else:
            b = tuple(box[k+1][0])
        cv2.line(image, a, b, (0, 255, 0))