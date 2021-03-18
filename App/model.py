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
    catalog = {'video': None,
               'category_id': None,
               'country': None,
               'trending_days': None,
               'tags': None,
               'likes': None
               'views': None}

catalog['video'] = lt.newList('SINGLE_LINKED', cmpVideos)
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
                                 maptype='CHAINING',
                                 loadfactor=0.5,
                                 comparefunction=cmpTags)

catalog['likes'] = mp.newMap(34500,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=cmpVideosByLikes)

catalog['views'] = mp.newMap(34500,
                                  maptype='PROBING',
                                  loadfactor=0.5,
                                  comparefunction=cmpVideosByViews)
return catalog




# Funciones para agregar informacion al catalogo





# Funciones para creacion de datos




# Funciones de consulta

def paisCategoria(catalog, category_ctg, category, country):
        cumple = lt.newList("ARRAY_LIST")
        for video in catalog["elements"]:
                if video["category_id"] == category_ctg[category] and video["country"] == country:
                        loadData(cumple,video)
        sublist = cumple.copy()
        return shellSortVideos(sublist,lt.size(sublist),'views')
 

def trendingpais(catalog,country):
        cumple = lt.newList("ARRAY_LIST")
        trending_days = {}
        videocopy = None
        for video in catalog["elements"]:
                if video["country"] == country:
                        if video['title'] in trending_days:
                                pos= int(trending_days[video['title']])
                                cumple['elements'][pos]['trending_days'] += 1
                        else:
                                videocopy = video.copy()
                                videocopy['trending_days'] = 1
                                trending_days[video['title']] = lt.size(cumple)
                                lt.addLast(cumple, videocopy)
 
        return shellSortVideos(cumple,lt.size(cumple),'trending_days')

def trendingcategory(catalog,category_ctg, category):
        cumple = lt.newList("ARRAY_LIST")
        trending_days = {}
        videocopy = None
        for video in catalog["elements"]:
                if video["category_id"] == category_ctg[category]:
                        if video['title'] in trending_days:
                                pos= int(trending_days[video['title']])
                                cumple['elements'][pos]['trending_days'] += 1
                        else:
                                videocopy = video.copy()
                                videocopy['trending_days'] = 1
                                trending_days[video['title']] = lt.size(cumple)
                                lt.addLast(cumple, videocopy)
 
        return shellSortVideos(cumple,lt.size(cumple),'trending_days')
                     
def likespaistag(catalog, country, tag):
        videos_tags = {}
        videotags = None
        cumple = lt.newList("ARRAY_LIST")
        for video in catalog["elements"]:
                if video['country'] == country:
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
                                                        if lt.size(cumple) == 0:
                                                                lt.removeFirst(cumple)
                                                                lt.addFirst(cumple, video)
                                                        else:
                                                                lt.deleteElement(cumple, pos)
                                                                lt.insertElement(cumple, video, pos)
                                        else:
                                                videos_tags[video['title']] = [lt.size(cumple),video['likes']]
                                                lt.addLast(cumple, video)
                                i += 1
        return shellSortVideos(cumple,lt.size(cumple),'likes')
                

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
def selectionSortVideos(catalog, size, parametro):
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        if parametro == 'trending_days':
                start_time = time.process_time()
                selectionSortList = sel.sort(sub_list, cmpVideosByTrendingdays)
                stop_time = time.process_time()
        elif parametro == 'views':
                start_time = time.process_time()
                selectionSortList = sel.sort(sub_list, cmpVideosByViews)
                stop_time = time.process_time()
        elif parametro == 'likes':
                start_time = time.process_time()
                selectionSortList = sel.sort(sub_list, cmpVideosByLikes)
                stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return (elapsed_time_mseg, selectionSortList)


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