class Capitulo:
    titulo = 'x'
    cantidadPaginas = 0
    def __init__(self, titulo = 'x', cantidadPaginas = 0):
        self.__titulo = titulo
        self.__cantidadPaginas = int(cantidadPaginas)
    def __str__(self):
        return "%s %d" % (self.__titulo, self.__cantidadPaginas)
    def getTitulo(self):
        return self.__titulo