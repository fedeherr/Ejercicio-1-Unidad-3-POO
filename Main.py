from Menu import Menu
from ManejadorLibros import manejaLibros
if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Ingresar el identificador de un libro y mostrar título del libro, nombre de cada uno de sus capítulos y cantidad total de páginas de un libro.
              2 Dada una palabra, mostrar título y autor de los libros que contienen la palabra dada en su título o en el título de alguno de sus capítulos.""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0