#!usr/bin/env python3
#-*- coding: utf-8 -*-

with open ('persons.txt', 'rt', encoding='utf-8') as trg:
    lines = trg.readlines()
    print(lines[-1])