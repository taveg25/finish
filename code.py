#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import qrcode
from datetime import datetime

familia = input('Фамилия: ')
number = input('Номер: ')
start_time = datetime.now()


stime = start_time

text = f'{{"familia":"{familia}","number":{number},"stime":"{stime}"}}'
if len(text) < 64:
    text += ' '*(64-len(text))
    
image = qrcode.make(text)

image.save(f'{familia}.png')