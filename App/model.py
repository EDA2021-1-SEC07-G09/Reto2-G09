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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qui 
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
        catalog = {'video': None,
                        'category_id': None,
                        'country': None}
 

        catalog['video'] = lt.newList('ARRAY_LIST')
        catalog['category_id'] = mp.newMap(34500,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        comparefunction=cmpCategoryId)
        catalog['country'] = mp.newMap(34500,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        comparefunction=cmpCountry)                                   
        

        return catalog

def newcategory():
        category = {}
        return category
# Funciones para agregar informacion al catalogo
def loadData(catalog,video):
        lt.addLast(catalog['video'], video)

def addVideoCountry(catalog, video):

        pais = catalog['country']
        paisvideo = video['country']
        existpais = mp.contains(pais, paisvideo)
        if existpais:
            entry = mp.get(pais, paisvideo)
            country = me.getValue(entry)
        else:
            country = lt.newList('ARRAY_LIST')
            mp.put(pais, paisvideo, country)
        lt.addLast(country, video)


def addVideoCatergory(catalog, video):

        category= catalog['category_id']
        categoryvideo = video['category_id']
        existcategory = mp.contains(category, categoryvideo)
        if existcategory:
            entry = mp.get(category, categoryvideo)
            categoria = me.getValue(entry)
        else:
            categoria = lt.newList('ARRAY_LIST')
            mp.put(category, categoryvideo, categoria)
        lt.addLast(categoria, video)



def loadCategory_id(category, category_id):
        name = category_id["name"].lstrip()
        category[name] = category_id['id']

# Funciones para creacion de datos

# Funciones de consulta

def paisCategoria(catalog, category_ctg, category, country):
        cumple = lt.newList("ARRAY_LIST")
        pais = mp.get(catalog["country"], country)
        videos = me.getValue(pais)
        for video in videos['elements']:
                if video["category_id"] == category_ctg[category]:
                        lt.addLast(cumple,video)
        sublist = cumple.copy()
        return mergeSortVideos(sublist,lt.size(sublist),'views')
 

def trendingpais(catalog,country):
        cumple = lt.newList("ARRAY_LIST")
        trending_days = {}
        videocopy = None
        pais = mp.get(catalog["country"], country)
        videos = me.getValue(pais)
        for video in videos["elements"]:
                        if video['title'] in trending_days:
                                pos= int(trending_days[video['title']])
                                cumple['elements'][pos]['trending_days'] += 1
                        else:
                                videocopy = video.copy()
                                videocopy['trending_days'] = 1
                                trending_days[video['title']] = lt.size(cumple)
                                lt.addLast(cumple, videocopy)
 
        return mergeSortVideos(cumple,lt.size(cumple),'trending_days')

def trendingcategory(catalog,category_ctg, category):
        cumple = lt.newList("ARRAY_LIST")
        trending_days = {}
        videocopy = None
        categoria = mp.get(catalog["category_id"], category_ctg[category])
        videos = me.getValue(categoria)
        for video in videos["elements"]:
                        if video['title'] in trending_days:
                                pos= int(trending_days[video['title']])
                                cumple['elements'][pos]['trending_days'] += 1
                        else:
                                videocopy = video.copy()
                                videocopy['trending_days'] = 1
                                trending_days[video['title']] = lt.size(cumple)
                                lt.addLast(cumple, videocopy)
 
        return mergeSortVideos(cumple,lt.size(cumple),'trending_days')
                     
def likespaistag(catalog, country, tag):
        videos_tags = {}
        videotags = None
        cumple = lt.newList("ARRAY_LIST")
        pais = mp.get(catalog["country"], country)
        videos = me.getValue(pais)
        for video in videos["elements"]:
                        videotags = video["tags"]
                        videotags = videotags.replace('"','')
                        videotags = videotags.split('|')
                        ejecutar = True
                        i = 0
                        while ejecutar == True and i < len(videotags):
                                if tag in videotags[i]:
                                        ejecutar = False
                                        if video['title'] in videos_tags:
                                                likes= int(videos_tags[video['title']][1])
                                                pos = int(videos_tags[video['title']][0])
                                                if int(video['likes']) > likes:
                                                        videos_tags[video['title']][1] = video['likes']
                                                        cumple['elements'][pos]['likes'] = video['likes']
                                        else:
                                                videos_tags[video['title']] = [lt.size(cumple),video['likes']]
                                                videocopy = video.copy()
                                                lt.addLast(cumple, videocopy)
                                i += 1
        return mergeSortVideos(cumple,lt.size(cumple),'likes')
                
                



# Funciones utilizadas para comparar elementos dentro de una lista
def cmpCategoryId(key, element):
        tagentry = me.getKey(element)
        if (str(key) == str(tagentry)):
                return 0
        else:
                return 1

def cmpCountry(key, element):
        tagentry = me.getKey(element)
        if (str(key) == str(tagentry)):
                return 0
        else:
                return 1 

def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

def cmpVideosByTrendingdays(video1, video2):
    return (float(video1['trending_days']) > float(video2['trending_days']))

def cmpVideosByLikes(video1, video2):
    return (float(video1['likes']) > float(video2['likes']))


def selectionSortVideos(catalog, size, parametro):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        if parametro == 'trending_days':
                selectionSortList = sel.sort(sub_list, cmpVideosByTrendingdays)
        elif parametro == 'views':
                selectionSortList = sel.sort(sub_list, cmpVideosByViews)
        elif parametro == 'likes':
                selectionSortList = sel.sort(sub_list, cmpVideosByLikes)
        return selectionSortList


def shellSortVideos(catalog, size, parametro):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        if parametro == 'trending_days':
                start_time = time.process_time()
                shellSortList = sa.sort(sub_list, cmpVideosByTrendingdays)
                stop_time = time.process_time()
        elif parametro == 'views':
                start_time = time.process_time()
                shellSortList = sa.sort(sub_list, cmpVideosByViews)
                stop_time = time.process_time()
        elif parametro == 'likes':
                start_time = time.process_time()
                shellSortList = sa.sort(sub_list, cmpVideosByLikes)
                stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, shellSortList)

def insertionSortVideos(catalog, size, parametro):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        if parametro == 'trending_days':
                start_time = time.process_time()
                insertionSortList = ins.sort(sub_list, cmpVideosByTrendingdays)
                stop_time = time.process_time()
        elif parametro == 'views':
                start_time = time.process_time()
                insertionSortList = ins.sort(sub_list, cmpVideosByViews)
                stop_time = time.process_time()
        elif parametro == 'likes':
                start_time = time.process_time()
                insertionSortList = ins.sort(sub_list, cmpVideosByLikes)
                stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, insertionSortList)
        
def quickSortVideos(catalog, size, parametro):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        if parametro == 'trending_days':
                start_time = time.process_time()
                quickSortList = qui.sort(sub_list, cmpVideosByTrendingdays)
                stop_time = time.process_time()
        elif parametro == 'views':
                start_time = time.process_time()
                quickSortList = qui.sort(sub_list, cmpVideosByViews)
                stop_time = time.process_time()
        elif parametro == 'likes':
                start_time = time.process_time()
                quickSortList = qui.sort(sub_list, cmpVideosByLikes)
                stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, quickSortList)

def mergeSortVideos(catalog, size, parametro):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        if parametro == 'trending_days':
                start_time = time.process_time()
                mergeSortList = mer.sort(sub_list, cmpVideosByTrendingdays)
                stop_time = time.process_time()
        elif parametro == 'views':
                start_time = time.process_time()
                mergeSortList = mer.sort(sub_list, cmpVideosByViews)
                stop_time = time.process_time()
        elif parametro == 'likes':
                start_time = time.process_time()
                mergeSortList = mer.sort(sub_list, cmpVideosByLikes)
                stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, mergeSortList)
# Funciones de ordenamiento