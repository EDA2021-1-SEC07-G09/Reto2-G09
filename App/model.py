"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
               'category_id': None,
               'country': None,
               'trending_days': None,
               'tags': None,
               'likes': None
               'views': None}

catalog['books'] = lt.newList('SINGLE_LINKED', compareBookIds)
catalog['category_id'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=cmpCategoryId)
catalog['country'] = mp.newMap(800,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=cmpCountry)                                   
catalog['trending_days'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=cmpVideosByTrendingdays)

catalog['tags'] = mp.newMap(40,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=cmpTags)

catalog['likes'] = mp.newMap(34500,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=cmpVideosByLikes)

catalog['views'] = mp.newMap(34500,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=cmpVideosByViews)
return catalog




# Funciones para agregar informacion al catalogo





# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideos (v1, v2):
    if (v1 == v2):
        return 0
    elif v1 > v2:
        return 1
    else :
        return -1


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

def cmpVideosByTrendingdays(video1, video2):
    return (float(video1['trending_days']) > float(video2['trending_days']))

def cmpVideosByLikes(video1, video2):
    return (float(video1['likes']) > float(video2['likes']))

def cmpCategoryId (keyname, categ):
    catEntry = me.getKey(categ)
    if (keyname == catEntry):
        return 0
    elif (keyname > catEntry):
        return 1
    else:
        return -1

def cmpCountry (keyname, country):
    countName = me.getKey(country)
    if (keyname == countName):
        return 0
    elif (keyname > countName):
        return 1
    else:
        return -1

def cmpTags (keyname, tags):
    tagName = me.getKey(tags)
    if (keyname == tagName):
        return 0
    elif (keyname > tagName):
        return 1
    else:
        return -1
    


# Funciones de ordenamiento
