# lab 2-1

n = int( input( "n="))
m = int( input( "m="))
if ( n < m):
    for i in range( n, m+1):
        print( i, end=" ")
    print()
else:
    print( f"n={n} больше равно m={m}")
