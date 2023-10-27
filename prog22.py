# lab 2-2

n = int( input( "n="))
if ( n < 0):
    print("введено отрицательное значение")
    exit() # не очень нужен
else:
    for i in range( n, n+11):
        print( i, end=" ")
print()