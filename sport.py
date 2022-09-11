#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import get

BEST_COUNT = 5
best = []

for person in get.all_persons_kbd():
    
    #Добавляем спортсмена в список
    best.append(person)
    
    #Сортируем список
    best.sort()
    if not get.check_equals(best):
        raise Exception('Результаты повторяются')
    
    #Удаляем лишний элемент
    if len(best) > BEST_COUNT:
        r, n, f = best[-1]
        with open('persons.txt', 'at', encoding='utf-8') as trg:
            print( f'{f},{n},{r:.2f}', file=trg)
        del best[-1]
    
    #Выводим список 
    #(вариант еще получше)
    print('-'*40)
    for k, x in enumerate(best, start=1):
        res, num, fam = x
        text = f'{k:2d}.{fam:12} {num:3d} - {res:6.2f}'
        print(text)
    print('-'*40)
    
#Сохраним лучших в файл
trg = open('best.txt', 'wt', encoding='utf-8')
try:
    for res, num, fam in best:
        print(f'{fam},{num},{res:.2f}', file=trg)
finally:
    trg.close()