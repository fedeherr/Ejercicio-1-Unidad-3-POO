from ManejadorLibros import manejaLibros
class Menu:
    __switcher=None
    __manejo = manejaLibros()
    def __init__(self):
        self.__manejo.manejarLibros()
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        ident = int(input("Ingrese el identificador del libro "))
        print(self.__manejo.opcion1(ident))
    def opcion2(self):
          palab = input("Ingrese palabra a buscar ")
          self.__manejo.opcion2(palab)