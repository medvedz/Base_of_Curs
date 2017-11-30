
 # Это все тестовый блок для проверки работоспособности алгоритмов

import Filters
import cv2 as cv

A=Filters.Filters(cv.imread('test_img/7_black.png',cv.IMREAD_GRAYSCALE))
B=Filters.Filters(cv.imread('test_img/1.png',cv.IMREAD_GRAYSCALE))

cv.imshow('A',A.picture)
cv.imshow('B',B.picture)

# пример работы линейных сгдаживающих фильтров
"""
            -- Описание для линейных сглаживающих фильтров --

При увеличении размера маски увеличивается рассеивание в обоих случаях

Однородная маска дает большее рассеивание 
Маска взвешенного среднего дает меньшее рассеивание 

Маска взята как квадратная для удобства реализации,
а именно для удобного подсчета отклика в случае отличных от 1 коэффициентов маски
т.к. нас интересует результат работы фильтров , а не форма маски
главное чтобы маска была размера (2a+1) x (2b+1)

"""

cv.imshow('A Line Filter (1)',A.SpaceFilter_line(5,0).picture)
cv.imshow('A Line Filter (avg)',A.SpaceFilter_line(5,1).picture)


cv.imshow('B Line Filter (1)',B.SpaceFilter_line(5,0).picture)
cv.imshow('B Line Filter (avg)',B.SpaceFilter_line(5,1).picture)



# пример работы нелинейных сгдаживающих фильтров
"""
    -------  Описание нелинейных сглаживающих фильтров  ---------
    
Медианный фильтр дает отличное подавление импульсных шумов, 
при малой расфокусировке

Фильтры макс. и мин. позволяют выделить области наибольшей и наименьшей яркости изображения


"""

cv.imshow('A Not Line Filter (median)',A.SpaceFilter_notline(3).picture)
cv.imshow('B Not Line Filter (median)',B.SpaceFilter_notline(3).picture)



# Линейный с однородной маской + Медианный
cv.imshow('Line Filter (1)  + Not Line Filter',A.SpaceFilter_line(5,0).SpaceFilter_notline(3).picture)
cv.imshow('Line Filter (avg)  + Not Line Filter',B.SpaceFilter_line(5,0).SpaceFilter_notline(5).picture)



# Линейный с усредняющей маской + Медианный
cv.imshow('Line Filter (avg)  + Not Line Filter',A.SpaceFilter_line(5,1).SpaceFilter_notline(3).picture)
cv.imshow('Line Filter (avg)  + Not Line Filter',B.SpaceFilter_line(5,1).SpaceFilter_notline(5).picture)

cv.waitKey(0)