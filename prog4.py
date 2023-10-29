# Построение хэш-таблицы

class HashTabl:

    def __init__( self):     
        self.__ht = {}
        self.__modKey = 1

    def setModKey( self, key):
        if ( key > 0):
            self.__modKey = key

    def __genKey ( self, s):
        sord = ""
        for c in s :
            k = ord( c)
            sord = sord + str( k)
        num = int( sord)
        key = num % self.__modKey
        skey = str( key)
        return skey

    def __add ( self, skey, s):
        if ( skey in self.__ht):
            self.__ht[ skey].append( s)
        else:
            t = []
            t.append( s)
            self.__ht[ skey] = t

    def add( self, s):
        key = self.__genKey( s)
        self.__add( key, s)

    def printHt( self):
        for key in self.__ht :
            print( "Ключ ", key, " соответствует строкам:")
            for j in self.__ht[ key]:
                print( j) 
            print()
        if (len( self.__ht) == 0):
            print( "Таблица пуста.")

    def find( self, st):
        key = self.__genKey( st)
        if (key in self.__ht.keys()):
            mas = self.__ht[ key]
            if ( st in mas):
                return key
            else:
                return ""
        else:
            return ""

    def delete( self, st):
        key = self.find( st)
        if (key != ""):
            mas = self.__ht[ key]
            cm = mas.count( st)
            for i in range( cm):
                mas.remove( st)
            if ( len( mas) == 0):
                del self.__ht[ key]
            print("Элемент(ы) удалён.")
        else:
            print("Элемент не найден")

# Интерфейс

def menu():
    k = 0
    s = ""
    print( "\n1 - Добавить элеменнт")
    print( "2 - Обойти дерево")
    print( "3 - Найти элемент")
    print( "4 - Удалить элемент")
    print( "0 - Выход")
    s = input( "Ваш выбор: ")
    if ( s.isdigit()):
        k = int( s)
        if ( 0 <= k <= 4):
            return k
        else:
             print( "Недопустимое значение")
    else:
        print( "Ввкденное значение не является числом")
    return -1    

# главная программа

myHt = HashTabl()
mk = int( input( "Введите коэффициент для построения ключа: "))
myHt.setModKey( mk)  

k = menu()
while ( k != 0):
    if ( k == 1):
        sf = input("Введите значение для добавления в таблицу: ")
        myHt.add( sf)

    elif ( k == 2):
       myHt.printHt()

    elif ( k == 3):
        sf = input("Укажите значение для поиска в таблице:")
        if ( myHt.find( sf) != ""):
            print( "Элемент найден.")
        else:
            print( "Элемент не найден.")

    elif ( k == 4):
       sf = input( "Удалить строку: ")
       myHt.delete( sf)

    else:
        break
    k = menu()
print( "Конец программы.")