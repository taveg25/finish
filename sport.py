#!/usr/bin/env python3
#-*- coding: utf-8 -*-

best = []

while True:
    #Ввод данных о спортсмене
    familia = input('Введите фамилию:')
    if familia == 'КОНЕЦ':
        break
    num = input('Введите номер спортсмена:')
    res = input('Введите результат:')
    num = int(num)
    res = float(res)
    person = (res, num, familia)
    
    #Добавляем спортсмена в список
    best.append(person)
    
    #Сортируем список
    best.sort()
    
    #Удаляем лишний элемент
    if len(best)>5:
        del best[-1]
    
    #Выводим список 
    #(вариант еще получше)
    print('-'*40)
    for k, x in enumerate(best, start=1):
        res, num, fam = x
        text = f'{k:2d}.{fam:12} {num:3d} - {res:6.2f}'
        print(text)
    print('-'*40)