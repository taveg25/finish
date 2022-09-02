#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import get

BEST_COUNT = 5
best = []

while True:
    #Ввод данных о спортсмене
    person = get.input_person_kbd('КОНЕЦ')
    if person is None:
        break
    
    #Добавляем спортсмена в список
    best.append(person)
    
    #Сортируем список
    best.sort()
    if not get.check_equals(best):
        raise Exception('Результаты повторяются')
    
    #Удаляем лишний элемент
    if len(best) > BEST_COUNT:
        del best[-1]
    
    #Выводим список 
    #(вариант еще получше)
    print('-'*40)
    for k, x in enumerate(best, start=1):
        res, num, fam = x
        text = f'{k:2d}.{fam:12} {num:3d} - {res:6.2f}'
        print(text)
    print('-'*40)