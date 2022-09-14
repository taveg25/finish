#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time
import logging
import json
import get
logging.basicConfig(level=logging.DEBUG)

from myvideo import initialize, finalize, frame_box

BEST_COUNT = 5
best = []
data_1 = 0

cap, qrDecoder = initialize()


try:
    while True:
        time.sleep(1.0/25.0)
        ret, image = cap.read()
        if ret:
            result = qrDecoder.detectAndDecode(image)
            data, box, corrected_image = result
            if len(data) > 0:
                frame_box(box,image)
                if data == data_1:
                    print('Повтор спортсмена')
                    continue
                logging.debug(f'{data}, {type(data)}')
                data_1 = data
                data = json.loads(data)
                logging.debug(f'{data}, {type(data)}')
                if data['familia'] == 'КОНЕЦ':
                    break
                person = get.input_person_video(data)
                best.append(person)
                best.sort()
                if len(best) > BEST_COUNT:
                    r, n, f = best[-1]
                    with open('persons.txt', 'at', encoding='utf-8') as trg:
                        print( f'{f},{n},{r:.2f}', file=trg)
                    del best[-1]
                print('-'*40)
                for k, x in enumerate(best, start=1):
                    res, num, fam = x
                    text = f'{k:2d}.{fam:12} {num:3d} - {res:6.2f}'
                    print(text)
                print('-'*40)
                
                
            cv2.imshow('My WEB camera', image)
        if cv2.waitKey(1) == 27:
            break
finally:
    finalize(cap)
    with open('best.txt', 'wt', encoding='utf-8') as trg:
        for res, num, fam in best:
            print(f'{fam},{num},{res:.2f}', file=trg)

