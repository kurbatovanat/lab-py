# Транспонирование матрицы

# import random

def input_matr( fileName):
    matr = []
    s = ""
    with open( fileName, "r", encoding = "utf8") as myFile :
        s = myFile.readline()
        m = int( s)
        print( "m=", m)
        s = myFile.readline()
        n = int( s)
        print( "n=", s)
        for i in range( m):
                # print(f"строка {m}")
            s = myFile.readline()
            mas = s.split( " ")
#            for sk in mas:
#                print(sk)

            row = []
            for j in range( n):
               
                x = int( mas[j])
                row.append(x)
            matr.append(row)
    return matr                                                                                                                                                                             


def print_matr( matr):
    m= len( matr)
    for i in range(m):
        n = len( matr[ i])
        for j in range(n):
            print( matr[i][j], end=" ")
        print()


def save_matr( matr, fileName, s2):
    with open( fileName, "a", encoding = "utf8") as myFile:
        print( s2, file=myFile)
        for i in range( len( matr)):
            for j in range( len( matr[i])):
                print( matr[i][j], end=" ", file=myFile)
            print(file=myFile)


def trans(a):
    b = []
    m = len( a)
    if ( m == 0):
        print( " матрица пуста")
        return []
    n = len( a[0])
    for j in range( n):
        temp = []
        for i in range(m):
#            print(i, j)
            temp.append( a[i][j])
        b.append( temp)
    return b


# главная программа 
# mf = int( input("rows m="))
# nf = int( input("cols n="))
af = input_matr('3.txt')

print("Исходная матрица")
print_matr( af)
save_matr( af, 'outmatr.txt', "source")

bf = trans( af)

print("результат транспонирования" )
print_matr( bf)
save_matr( bf, 'outmatr.txt', "result")
print( "end of program")
                                                                                                                                                                                  