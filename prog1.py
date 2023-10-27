# Транспонирование матрицы

import random

def input_matr(m, n):
    matr = []
    for i in range(m):
            # print(f"строка {m}")
        row = []
        for j in range(n):
            x =  random.randint( 0, 100) # input(r"element {m},{n}")
            row.append(x)
        matr.append(row)
#        print( len( matr), len( row))
    return matr                                                                                                                                                                             


def print_matr( matr, m, n):
#    print("pm m=", m, " n=", n)
#    print("len matr ", len( matr))
    for i in range(m):
        for j in range(n):
            print( matr[i][j], end=" ")
        print()


def trans(a, m, n):
    b = []
    for j in range(n):
        temp = []
        for i in range(m):
#            print(i, j)
            temp.append( a[i][j])
        b.append( temp)
    return b


# главная программа 
mf = int( input("rows m="))
nf = int( input("cols n="))
af = input_matr(mf, nf)

print("Исходная матрица")
 print_matr(af, mf, nf)
bf = trans( af, mf, nf)

print("результат транспонирования" )
print_matr( bf, nf, mf)
print("end of program")                                                                                                                                                                                  