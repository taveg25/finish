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
    print(best)