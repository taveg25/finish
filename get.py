#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal

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