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
    print("6- Consultar X videos con más likes en un país con un tag específico")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        size = int(input("Inserte el número de videos: "))

    elif int(inputs[0]) == 3:
    pais = str(input("Inserte un país: "))
    categ = str( input("Inserte una categoría: "))
    size = int(input("Inserte el número de videos: "))

    elif int(inputs[0]) == 4:
        pais = str(input("Inserte una pais: "))

    elif int(inputs[0]) == 5:
        categ = str(input("Inserte una categoria: "))

    elif int(inputs[0]) == 6:
        size = int(input("Inserte el número de videos: "))
        pais = str(input("Inserte un país: "))
        tag = str(input("Inserte un tag específico: "))

    elif int(inputs[0]) == 7:
        size = int(input("Inserte el número de videos: "))
        categ = str( input("Inserte una categoría: "))
        

    else:
        sys.exit(0)
sys.exit(0)
