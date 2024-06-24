import json

def abrir_archivo():
    with open('biblioteca.json', 'r', encoding='utf-8') as archivo:
        lector = json.load(archivo)
        return lector
    
def menu_principal():
    print('*** MUNDO LIBRO ***')
    print('[1] - Mantenedores')
    print('[2] - Reportes')
    print('[3] - Salir')
    ejecutar_menu()

def menu_mantenedores():
    print('*** MENU MANTENEDORES ***')
    print('[1] - Agregar libro')
    print('[2] - Editar libro')
    print('[3] - Eliminar libro')
    print('[4] - Buscar libros')
    print('[5] - Mostra  todos los libros')
    print('[0] - ***Menu Principal***')

def ejecutar_menu():
    while True:
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            menu_mantenedores()
            opcion = input('Ingrese una opcion: ')
            if opcion == '1':
                agregar_libro()
                menu_mantenedores()
            if opcion == '2':
                editar_libro()
                menu_mantenedores()
            if opcion == '3':
                eliminar_libro()
                menu_mantenedores()
            if opcion == '4':
                print('EN TRABAJO')
                menu_mantenedores()
            if opcion == '5':
                mostrar_libros()
                menu_mantenedores()

        if opcion == '2':
            print('***REPORTES***')
        if opcion == '3':
            print('Has salido del programa')
            break
        if opcion == '0':
            menu_principal()

#read
def mostrar_libros():
    print('*** LIBROS DISPONIBLES ***')
    for i in diccionario['Libro']:
        print(i['Titulo'])


#create
def agregar_libro():
    print('*** AGREGAR LIBRO ***')
    id_libro = int(len(diccionario['Libro']) + 1)
    id_autor = int(len(diccionario['Autor']) + 1)
    #id_categoria = int(len(diccionario['CategoriaID']) + 1)
    titulo = input('Ingrese titulo de libro: ')
    anno_publicacion = int(input('Ingrese año de publicacion: '))
    isbn = int(input('Ingrese ISBN: '))

    agregar_datos = {
        "LibroID":id_libro,
        'Titulo':titulo,
        'AutorID':id_autor,
        #'CategoriaID':id_categoria,
        'AnoPublicacion':anno_publicacion,
        'ISBN':isbn
    }

    diccionario['Libro'].append(agregar_datos)
    print('*** AGREGADO CON EXITO ***')
    menu_principal()
    return diccionario


#update
def editar_libro():
    print('*** EDITAR LIBRO ***')
    id_libro = int(input('Ingrese ID de libro a modificar: '))
    nombre = input('Modificar el titulo: ')
    diccionario['Libro'][id_libro - 1]['Titulo'] = nombre
    print('*** MODIFICADO CON EXITO ****')

    return diccionario

#delete
def eliminar_libro():
    id_libro = int(input('Ingrese ID de libro para eliminarlo: '))
    diccionario['Libro'].pop(id_libro - 1)  
    print('*** ELIMINADO CON EXITO ***')     
    menu_principal()
    return diccionario          


diccionario = abrir_archivo()
diccionario = menu_principal()













    