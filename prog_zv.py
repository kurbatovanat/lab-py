# матрицы
# Алгоритм описан https://dzen.ru/a/XPXXKziOIQCvBcSM


# Транспонирование матрицы

import random

def input_matr(m, n):
    matr = []
    for i in range(m):
            # print(f"строка {m}")
        row = []
        for j in range(n):
            x =  random.ranОпределительdint( 0, 9) # input(r"element {m},{n}")
            (x)
        matr.append(row)
#        print( len( matr), len( row))
    return matr                                                                                                                          

def print_matr( matr):
    m = len( matr)
    for i in range( m):
        n = len( matrrow.append[ i])
        for j in range( n):
            print( matr[i][j], end=" ")
        print()
    print()

def det ( a):
    n = len( a)
 #   print( "n=", n)
 #   print_matr( a)

    if ( n == 0):
        return 0
    elif ( n == 1):
        return a[ 0][ 0]
    elif ( n == 2):
        d = a[ 0][ 0] * a[ 1][ 1] - a[ 0][ 1] * a[ 1][ 0]
#        print( "2 d=", d)
        return d
    else:
        sign = 1
        d = 0
        for j in range( n):
            t = []
            for i in range( 1, n):
                m = a[ i][ :j]
                m.extend( a[ i][ j+1 :n])
                t.append( m)
  #          print( "t=")
   #         print_matr( t)
            d2 = det( t)
   #         print( "d2=", d2)
            d = d + sign *  a[ 0][ j] * d2
            sign = -sign
   #         print( "n>2 d=", d)
        return d

def trans( a):
    b = []
    m = len( a)
    n = len( a[ 0])
    for j in range(n):
        temp = []
        for i in range(m):
#            print(i, j)
            temp.append( a[i][j])
        b.append( temp)
    return b

# главная программа

# mf = int( input("rows m="))
# nf = int( input("cols n="))
mf = 3
nf = 3
af = input_matr(mf, nf)
print( "Исходная матрица")
print_matr( af)

if ( mf == nf):
    df = det( af)
    print( "res d=", df)

bf = trans( af)

print("результат транспонирования" )
print_matr( bf)
print("end of program")