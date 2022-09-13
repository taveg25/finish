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