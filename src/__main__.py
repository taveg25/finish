#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sport
import video

a = input('введите v для использования камеры,/n
            k для ввода данных с клавиатуры')
if a == 'v':
    video.video()
elif a == 'k':
    sport.sport()
else:
    print('Выбор неочевиден. запустите программу заново')

