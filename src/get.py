#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import datetime

TEMPLATE = Decimal('0.01')

def input_person_kbd(final_mark):
    f = input('Фам: ')
    if f == final_mark:
        return None
    n = input('Ном: ')
    r = input('Рез: ')
    r = Decimal(r)
    r = r.quantize(TEMPLATE)
    return (r, int(n), f)

def all_persons_kbd():
    while True:
        p = input_person_kbd('КОНЕЦ')
        if p is None:
            break
        yield p
        
def input_person_video(data, final_mark='КОНЕЦ'):
    f = data['familia']
    if f == final_mark:
        return None
    n = data['number']
    tstart = datetime.strptime(data['stime'], 
                                '%Y-%m-%d %H:%M:%S.%f')
    r = datetime.now() - tstart
    r = r.total_seconds()
    r = Decimal(r)
    r = r.quantize(TEMPLATE)
    return (r, int(n), f)

def all_persons_video(data):
    while True:
        p = input_person_video(data)
        if p is None:
            break
        yield p
    
def check_equals(people):
    iterator = iter(people)
    x = next(iterator)
    r1 = x[0]
    for y in iterator:
        r2 = y[0]
        if r1 == r2:
            return False
        r1 = r2
    return True