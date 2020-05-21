import csv
from Libro import Libro
from Capitulo import Capitulo
class manejaLibros:
    __listaLibros = []
    def __init__ (self, listaLibros = []):
        self.__listaLibros = listaLibros
    def agregarLibro(self, unLibro):
        self.__listaLibros.append(unLibro)
    def __str__(self):
        s = ""       
        for libro in self.__listaLibros:
            s += str(libro) + '\n'
            s += libro.stringcapitulos() + '\n'
        return s
    def opcion1(self, identificador):
        s = ""       
        for libro in self.__listaLibros:
            if (libro.getIdentificador() == identificador):
                s += 'El titulo es ' + str(libro.getTitulo()) + '\n'
                s += 'Y sus capitulos son:\n' + libro.stringcapitulos() + '\n'
        return s
    def opcion2(self, palabra):
        s = ""       
        for libro in self.__listaLibros:
            s += str(libro.getTitulo()) + '\n'
            s += libro.stringcapitulosTitulos() + '\n'
            texto = s.split()
            if palabra in texto:
                print ("Esta palabra se encontró dentro del libro " + libro.getTitulo() + " escrito por " + libro.getAutor())
            s = ""
    def manejarLibros(self):
        archivo = open('Libros.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        idLibro = 0
        cuentacaps = 0
        for fila in reader:
            if bandera:
                "'saltear cabecera'"
                bandera = not bandera
            else:
                if (str.isdigit(fila[5])):
                    cuentacaps = 0
                    idLibro = fila[0]
                    titulo = fila[1]
                    autor = fila[2]
                    editorial = fila[3]
                    isbn = fila[4]
                    capitulos = int(fila[5])
                    unLibro = Libro(idLibro, titulo, autor, editorial, isbn, capitulos)
                if (idLibro != fila[0]): #Para no hacer que un libro sea su propio capitulo
                    titulo = fila[0]
                    cantidadpaginas = fila[1]
                    unCapitulo = Capitulo(titulo,cantidadpaginas)
                    unLibro.setCapitulo(unCapitulo)
                    cuentacaps = cuentacaps + 1
                    if (cuentacaps == capitulos):
                        self.agregarLibro(unLibro)
                        cuentacaps = 0
                