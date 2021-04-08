"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar X videos con más views")
    print("3: Consultar los X videos mas vistos en un pais para una categoría")
    print("4- Consultar el video que más días fue trending para un país")
    print("5- Consultar el video que más días fue trending para una categoría")
    print("6- Consultar X videos con más likes en un país con un tag específico")
    print("0- Salir")

def initCatalog():
    return controller.initCatalog()
    
def initcategory():
    return controller.initcategory()

def loadData(catalog, category):
    controller.loadData(catalog, category)

def printResults(ord_videos, n:int, inputs:int):

    if inputs == 2 and n <= lt.size(ord_videos):
        print("Los primeros ", n, " videos ordenados son: ")
        i = 1
        while i <= n:
            video = lt.getElement(ord_videos, i)
            print("Titulo : "+ video['title'] + ' Titulo del Canal: '+ video['channel_title'] +
            ' Trending_date: ' + video['trending_date']+ ' Pais: '+ video['country'] +
            ' views: '+ video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: ' + video['dislikes']+ ' Fecha de publicación: '+video['publish_time'])
            i += 1
    elif inputs == 3 and n <= lt.size(ord_videos):
        i = 1
        while i <= n:
            video = lt.getElement(ord_videos, i)
            print(' Trending_date: ' + video['trending_date']+ " Titulo : "+ video['title']+ 
            ' Titulo del Canal: '+ video['channel_title'] + ' Fecha de publicación: '+video['publish_time']+ 'views: '+ video['views'] + ' Likes: ' +
             video['likes'] + ' Dislikes: ' + video['dislikes'])
            i += 1
    elif inputs == 4 and n <= lt.size(ord_videos):
        i = 1
        while i <= n:
            video = lt.getElement(ord_videos, i)
            print(" Titulo : "+ video['title']+ ' Titulo del Canal: '+ video['channel_title'] + ' Pais: '+
            video['country']+ ' Dias de tendencia: ', video['trending_days'])
            i += 1
    elif inputs == 5 and n <= lt.size(ord_videos):
        i = 1
        while i <= n:
            video = lt.getElement(ord_videos, i)
            print(" Titulo : "+ video['title']+ ' Titulo del Canal: '+ video['channel_title'] + ' Categoria_id: '+
            video['category_id']+ ' Dias de tendencia: ', video['trending_days'])
            i += 1
    if inputs == 6 and n <= lt.size(ord_videos):
        i = 1
        while i <= n:
            video = lt.getElement(ord_videos, i)
            print("Titulo : "+ video['title'] + ' Titulo del Canal: '+ video['channel_title'] + ' Pais: '+ video['country'] +
            ' Fecha de publicación: '+video['publish_time'] + ' views: '+ video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: ' + 
            video['dislikes'] + ' Tags: ' + video['tags'])
            i += 1
"""
Menu principal
"""
while True:
    printMenu()
    opcion = input('Seleccione una opción para continuar\n')
    inputs = int(opcion[0])
    if inputs == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        category_ctg = initcategory()
        answer = loadData()
        print('Videos cargados: ' + str(lt.size(catalog['video'])))
        print('Catalagos cargados: ' + str(len(category_ctg)))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
        

    elif inputs== 2:
        size = int(input("Inserte el número de videos: "))
        print('Metodo de ordenamiento que desea utilizar')
        print('1- shellsort')
        print('2- selectionsort')
        print('3- insertionsort')
        print('4- mergesort')
        print('5- quicksort')
        typesort = input('Seleccione el metodo de ordenamiento para continuar\n')
        result = None
        if size <= lt.size(catalog):
            if int(typesort[0]) == 1:
                result = controller.shellSortVideos(catalog, (size))
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1],10,inputs)
                
            elif int(typesort[0]) == 2:
                result = controller.selectionSortVideos(catalog, size)
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1],10,inputs)
            
            elif int(typesort[0]) == 3:
                result = controller.insertionSortVideos(catalog, size)
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1],10,inputs)
            elif int(typesort[0]) == 4:
                result = controller.mergeSortVideos(catalog, size)
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1],10,inputs)
            elif int(typesort[0]) == 5:
                result = controller.quickSortVideos(catalog, size)
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
                printResults(result[1],10,inputs)

    elif inputs == 3:
        pais = str(input("Inserte un país: "))
        categ = str( input("Inserte una categoría: "))
        size = int(input("Inserte el número de videos: "))
        result = controller.paisCategoria(catalog, category_ctg, categ, pais)
        print("Los primeros ", size, " videos ordenados por views de ",pais, "que pertenecen a la categoría ",
        categ, " son: ")
        printResults(result[1],size,inputs)

    
    elif inputs == 4:
        pais = str(input("Inserte una pais: "))
        result = controller.trendingpais(catalog,pais)
        print("El video que fue trending mas dias de ", pais, " es: ")
        printResults(result[1],1,inputs)

    elif inputs == 5:
        categ = str(input("Inserte una categoria: "))
        result = controller.trendingcategory(catalog, category_ctg, categ)
        print("El video que fue trending mas dias de la categoría ", categ, " es: ")
        printResults(result[1],1,inputs)

    elif inputs == 6:
        size = int(input("Inserte el número de videos: "))
        pais = str(input("Inserte un país: "))
        tag = str(input("Inserte un tag específico: "))
        result = controller.likespaistag(catalog, pais, tag)
        print("Los primeros ", size, " videos diferentes de ", pais, " con el tag ", tag, " con mas likes son: ")
        printResults(result[1],size,inputs)
    else:
        sys.exit(0)
sys.exit(0)
