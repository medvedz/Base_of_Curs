
 # Это все тестовый блок для проверки работоспособности алгоритмов

import Filters
import Masks
import cv2 as cv

A=Filters.Filters(cv.imread('test_img/7_black.png',cv.IMREAD_GRAYSCALE))
B=Filters.Filters(cv.imread('test_img/bigtest.png',cv.IMREAD_GRAYSCALE))
C=Filters.Filters(cv.imread('test_img/bird.png',cv.IMREAD_GRAYSCALE))
D=Filters.Filters(cv.imread('test_img/lap.png',cv.IMREAD_GRAYSCALE))
E=Filters.Filters(cv.imread('test_img/lap.png',cv.IMREAD_GRAYSCALE))

#cv.imshow('D',D.picture)
#cv.imshow('A',A.picture)
#cv.imshow('B',B.picture)
#cv.imshow('E',E.picture)

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

#cv.imshow('A Line Filter (1)',A.SpaceFilter_line(5,0).picture)
#cv.imshow('A Line Filter (avg)',A.SpaceFilter_line(5,1).picture)


#cv.imshow('B Line Filter (1)',B.SpaceFilter_line(5,0).picture)
#cv.imshow('B Line Filter (avg)',B.SpaceFilter_line(5,1).picture)



# пример работы нелинейных сгдаживающих фильтров
"""
    -------  Описание нелинейных сглаживающих фильтров  ---------
    
Медианный фильтр обычно используется для уменьшения шума или «сглаживания» изображения.
    
Медианный фильтр дает отличное подавление импульсных шумов, 
при малой расфокусировке

Эрозия увеличивает темные тона , а наращивание светлые.


"""

#cv.imshow('A Not Line Filter (median)',A.SpaceFilter_notline(3).picture)
#cv.imshow('B Not Line Filter (min)',B.SpaceFilter_notline(3,1).picture)
#cv.imshow('B Not Line Filter (max)',B.SpaceFilter_notline(3,2).picture)
#cv.imshow('B Not Line Filter (median)',B.SpaceFilter_notline(3).picture)



# Линейный с однородной маской + Медианный
#cv.imshow('Line Filter (1)  + Not Line Filter',A.SpaceFilter_line(5).SpaceFilter_notline(3).picture)
#cv.imshow('Line Filter (avg)  + Not Line Filter',B.SpaceFilter_line(5).SpaceFilter_notline(5).picture)



# Линейный с усредняющей маской + Медианный
#cv.imshow('Line Filter (avg)  + Not Line Filter',A.SpaceFilter_notline(3).SpaceFilter_line(5,1).picture)
#cv.imshow('Line Filter (avg)  + Not Line Filter',B.SpaceFilter_line(5,1).SpaceFilter_notline(5).picture)


#cv.imshow('D line',D.SpaceFilter_line(3).picture)
#cv.imshow('D 90',D.SpaceFilter_laplacian().picture)
#cv.imshow('D 45',D.SpaceFilter_laplacian(1).picture)
#cv.imshow('D median',D.SpaceFilter_notline(3).picture)



#cv.imshow('D median + 45',D.SpaceFilter_notline(3).SpaceFilter_laplacian(1).picture)
#cv.imshow('D 45 + median',D.SpaceFilter_laplacian(1).SpaceFilter_notline(3).picture)

#cv.imshow('D line + 90',D.SpaceFilter_line(3).SpaceFilter_laplacian().picture)

#cv.imshow('D line + 90 ',D.SpaceFilter_line(3,1).SpaceFilter_laplacian().picture)
#cv.imshow('A line + 45',A.SpaceFilter_line(3,1).SpaceFilter_laplacian(1).picture)

#cv.imshow('E sobel',E.SpaceFilter_sobel().picture)



cv.waitKey(0)

