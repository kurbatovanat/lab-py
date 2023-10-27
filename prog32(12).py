class BinTree :
    def __init__( self):
        self.__root = None

    def __createNode( self, inf, parentNode):
        temp = { "left" : None, "right" : None}
        temp[ "value"] = inf
        temp[ "parent"] = parentNode
        return temp

    def __add ( self, inf, tree, parentNode): 
        temp = tree 
        if (tree == None): 
            temp = self.__createNode( inf, parentNode)
            if ( self.__root == None): 
                self.__root = temp 
        elif ( inf < tree[ "value"]): 
            temp[ "left"] = self.__add( inf, tree[ "left"], tree) 
        elif ( inf > tree[ "value"]): 
            temp[ "right"] = self.__add( inf, tree[ "right"], tree) 
        else: 
            print("Такой элеиент уже есть в дереве.") 
        return temp 

    def add( self, inf):
        self.__add( inf, self.__root, None)

    def __obhod ( self, tree): 
        if ( tree != None): 
            self.__obhod( tree[ "left"]) 
            print( tree[ "value"], end=" ") 
            self.__obhod( tree[ "right"]) 

    def obhod( self):
        if ( self.__root != None):
            self.__obhod( self.__root)
            print()
        else:
            print( "Дерево пусто.")

    def __obhod2( self, tree):
        if ( tree != None): 
            self.__obhod2( tree[ "left"]) 
            print( tree[ "value"], end=" ") 
            t = tree[ "parent"] 
            if ( t != None):
                print( "родитель ", t[ "value"])
            else:
                 print( "родитнль пуст")
            self.__obhod2( tree[ "right"]) 

    def obhod2( self):
        if ( self.__root != None):
            self.__obhod2( self.__root)
            print()
        else:
            print( "Дерево пусто.")


    def __find( self, el): # возвращает ссылку на найденный узел
        temp = self.__root
        while ( temp != None):
            if ( el > temp[ "value"]):
                temp = temp[ "right"]
            elif ( el < temp[ "value"]):
                temp = temp[ "left"]
            else:
                return temp
        return temp


    def find( self, elem):
        if ( self.__find( elem) != None):
            print( "Элемент найден.")
            return True
        else:
            print( "Элемента нет в дереве.")
            return False 

    def isempty( self):
        return self.__root == None

             
    def __delNode( self, deleting):
        if ( deleting == None):
            print( "Попытка удвлить несуществующий узел")
            return False
        tleft = deleting[ "left"]
        tright = deleting[ "right"]
        tparent = deleting[ "parent"]
        if ( tright == None):
            if ( tparent != None):
                if ( deleting[ "value"] < tparent[ "value"]):
                    tparent[ "left"] = tleft
                else:
                    tparent[ "right"] = tleft
            else:
                self.__root = tleft
            if ( tleft != None):
                tleft[ "parent"] = tparent
        else:
            tright[ "parent"] = tparent
            if ( tparent != None):
                if ( deleting[ "value"] > tparent[ "value"]):
                    tparentt[ "right"] = tright
                else:
                    tparent[ "left"] = tright
            else:
                self.__root = tright
            if ( tleft != None):
                temp = tright
                while ( temp[ "left"] != None):
                    temp = temp[ "left"]
                temp[ "left"] = tleft
                tleft[ "parent"] = temp
        temp = deleting
        temp.clear()
        return True

    def delete( self, elem):
        temp = self.__find( elem)
        if ( temp != None):
            if self.__delNode( temp):
                print( "Элемент удален.")
                return True
            else:
                print( "Элемент найден, но не удален.")
                return False
        else:
            print( "Элемент не найден.")
            return False

# Интерфейс

def menu():
    k = 0
    s = ""
    print( "1 - Добавить элеменнт")
    print( "2 - Обойти дерево")
    print( "3 - Найти элемент")
    print( "4 - Удалить элемент")
    print( "5 - Показать родительские узлы")
    print( "0 - Выход")
    s = input( "Ваш выбор: ")
    if ( s.isdigit()):
        k = int( s)
        if ( 0 <= k <= 5):
            return k
        else:
             print( "Недопустимое значение")
    else:
        print( "Ввкденное значение не является числом")
    return -1    

# Главная

myTree = BinTree()
k = menu()
while ( k != 0):
    if ( k == 1):
       el = int( input( "Добавить el="))
       myTree.add( el)
    elif ( k == 2):
       myTree.obhod()
    elif ( k == 3):
       el = int( input( "Найти el="))
       myTree.find( el) 
    elif ( k == 4):
       el = int( input( "Удалить el="))
       myTree.delete( el)
    elif ( k == 5):
        myTree.obhod2()
    else:
        break
    k = menu()
print( "Конец")