# lab 3.1

import random

def genMas( k, n, m):
    mas = []
    for i in range( k):
        x = random.randint( n, m)
        while (x in mas):
            x = random.randint( n, m)
        mas.append( x)
    return mas


def find( j, mas):
    l = 0
    r = len( mas)
    while (l < r):
        i = (l + r)// 2
        if( j < mas[ i]):
            r = i
        elif ( j > mas[ i]):
            l = i + 1
        else:
            return i
    return -1


# главная
kf = int( input( "Размер массива k="))
nf = int( input( "Нижняя граница диапазона n="))
mf = int( input( "Верхняя граница диапазона m="))
if ( nf >= mf):
    print("Неверные границы диапазона")
    exit()
masf = genMas( kf, nf, mf)
print("Исходный массив:")
print( masf)
masf.sort()
print( "Отсортированный массив:")
print( masf)
jf = int( input( "Искомый элемент j="))
res = find( jf, masf)
if ( res >= 0):
    print( "Индекс найденного элемента res=", res)
else:
    print( "Элемент не найден")
print( "Конец программы")







