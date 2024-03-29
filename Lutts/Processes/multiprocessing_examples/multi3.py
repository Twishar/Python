#распред заданий между процессами

import os
from multiprocessing import Process, Value, Array

procs = 3                           #глобальные переменные, отдельные для каждого процесса,
count = 0                           #не являются совместно используемыми

def showdata(label, val, arr):
    #Выводит значения данныъх в этом процессе

    msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
    print(msg % (label, os.getpid(), count, val.value, list(arr)))

def updater(val, arr):
    #обменивается данными через разделяемую память

    global count
    count += 1                  #глобальный счетчик недоступен другим процессам
    val.value += 1              #а передаваемый в обьекте - доступен
    for i in range(3): arr[i] += 1

if __name__ == '__main__':
    scalar = Value('i', 0)          #разделяемая память: предусматривает
                                    #синхронизацию процессов/потоков
    vector = Array('d', procs)      #коды типов из ctypes: int, double

    #вывести начальные значения в родительском процессе
    showdata('parent start', scalar, vector)

    #породить дочерний процесс, передать данные в разделяемой памяти
    p = Process(target=showdata, args=('child', scalar, vector))
    p.start(); p.join()

    #изменить значения в родителе и передать через разделяему память,
    #ждать завершения каждого потомка
    #все потомки видят изменения, выполненные в родительском процессе и
    #переданные в виде аргументов (но не глобальной памяти)

    print('\nloop1 (updates in parent, serial children)...')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start(); p.join()

    #то же самое, но потомки запускаются параллельно
    # все они видят результат последней итерации, потому то они хранятся
    #в совместно используемых обьектах

    print('\nloop2 (updates in parent, parallel children)...')
    ps = []

    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' %i), scalar, vector))
        p.start()
        ps.append(p)

    for p in ps: p.join()

    #обьекты в разделяемой памяти изменяются потомками,
    #ждать завершения каждого из них

    print('\nloop3 (updates in serial children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
        showdata('parent temp', scalar, vector)

    #то же самое, но потомки запускаются параллельно

    ps = []
    print('\nloop4 (updates in parallel children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps: p.join()

    #глобальная переменная count=6 доступна только родителю
    #выведет последние результаты #scalar = 12: +6 в родителе, +6 в 6 потомках
    showdata('parent end', scalar, vector)  #array[i] = 8:
                                            #+2 в родителе, +6 в 6 потомках
