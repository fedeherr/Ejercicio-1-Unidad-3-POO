from Capitulo import Capitulo
class Libro:
    idLibro = 0
    titulo = 'x'
    autor = 'x'
    editorial = 'x'
    isbn = 0
    cantidadCapitulos = 0
    capitulos = []
    def __init__(self, idLibro = 0, titulo = 'x', autor = 'x', editorial = 'x', isbn = 0, cantidadCapitulos = 0, capitulos = []):
        self.__idLibro = int(idLibro)
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isbn = int(isbn)
        self.__cantidadCapitulos = int(cantidadCapitulos)
        self.__capitulos = []
    def setCapitulo(self, unCapitulo):
        self.__capitulos.append(unCapitulo)
    def __str__(self):
        return "%d %s %s %s %d %d" % (self.__idLibro, self.__titulo, self.__autor, self.__editorial, self.__isbn, self.__cantidadCapitulos)
    def stringcapitulos(self):
        s = ""       
        for capitulo in self.__capitulos:
            s += str(capitulo) + '\n'
        return s
    def stringcapitulosTitulos(self):
        s = ""       
        for capitulo in self.__capitulos:
            s += str(capitulo.getTitulo()) + '\n'
        return s
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getIdentificador(self):
        return self.__idLibro

