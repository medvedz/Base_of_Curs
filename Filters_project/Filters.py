import cv2 as cv
import numpy as np
import matplotlib as mp
import Masks
import copy
import math as mt

BYTE = 256

class Filters(object):
    def __init__(self, _pict):
        self.picture = _pict
        self.heigth, self.width = _pict.shape
        self.size = self.heigth * self.width

    def GetHistogram(self):
        self.histogram = [0 for i in range(BYTE)]
        for row in range(self.heigth):
            for col in range(self.width):
                self.histogram[self.picture[row, col]] += 1
        return self.histogram

    def HistEqualization(self):
        if (not self.histogram):
            self.GetHistogram()
        equhist = [0 for i in range(BYTE)]
        for k in range(BYTE):
            for i in range(k):
                equhist[k] += self.histogram[i] / self.size
        return equhist

    def Filter_Hist(self, f_str="256*x"):
        if (not self.histogram):
            self.GetHistogram()
        equhist = self.HistEqualization()
        resimg = np.zeros(self.picture.shape, np.uint8)
        for row in range(self.heigth):
            for col in range(self.width):
                x = equhist[self.picture[row, col]]
                resimg[row, col] = eval(f_str)
        return resimg

    """
        Этот метод упрощенная версия 
    метода для однородной маски сглаживающего фильтра
        
    def SpaceFilter_one(self,n):
       resimg=self
       m=Masks.Mask(n)
       m.fill_one()
       R=0

       start_h=int(m.heigth/2)
       start_w = int(m.width / 2)

       end_h=resimg.heigth-int((m.heigth-1)/2)
       end_w=resimg.width-int((m.width-1)/2)

       for x in range(start_h,end_h):
           for y in range(start_w,end_w):
               R=0
               for i in range(int((m.heigth+1)/2)):
                   for j in range(int((m.width+1) / 2)):
                       R += (resimg.picture[x + i][y + j])
                       R += (resimg.picture[x - i][y + j])
                       R += (resimg.picture[x + i][y - j])
                       R += (resimg.picture[x - i][y - j])
               R -= (3*resimg.picture[x][y])
               for i in range(1,int((m.heigth + 1) / 2)):
                    R -= (resimg.picture[x + i][y])
                    R -= (resimg.picture[x - i][y])
               for j in range(1,int((m.width + 1) / 2)):
                    R -= (resimg.picture[x][y + j])
                    R -= (resimg.picture[x][y - j])
               R *= m.avg_k()
               resimg.picture[x][y]=R
       return resimg
    """

    def SpaceFilter_line(self, n,flag=0):  #0- однородная маска,  другие значения- среднее
        resimg = copy.deepcopy(self)
        m = Masks.Mask(n)
        if (flag==0):
            m.fill_one()
        else:
            m.fill_avg()
        R = 0

        # для проверки
        """
        m.print()
        print(m.add_k())
        print(m.avg_k())
        """

        start_h = int((m.heigth-1) / 2)
        start_w = int((m.width-1) / 2)

        end_h = resimg.heigth - start_h
        end_w = resimg.width - start_w

        for x in range(start_h, end_h):
            for y in range(start_w, end_w):
                R=0
                for i in range(int((m.heigth+1) / 2)):
                    for j in range(int((m.width+1) / 2)):
                        R += ((resimg.picture[x + i][y + j])*(m.mask[start_h+i][start_w+j]))
                        R += ((resimg.picture[x - i][y + j])*(m.mask[start_h-i][start_w+j]))
                        R += ((resimg.picture[x + i][y - j])*(m.mask[start_h+i][start_w-j]))
                        R += ((resimg.picture[x - i][y - j])*(m.mask[start_h-i][start_w-j]))
                R -= (3 * (resimg.picture[x][y])*(m.mask[start_h][start_w]))
                for i in range(1,int((m.heigth + 1) / 2)):
                      R -= ((resimg.picture[x + i][y])*(m.mask[start_h+i][start_w]))
                      R -= ((resimg.picture[x - i][y])*(m.mask[start_h-i][start_w]))
                for j in range(1,int((m.width + 1) / 2)):
                      R -= ((resimg.picture[x][y + j])*(m.mask[start_h][start_w+j]))
                      R -= ((resimg.picture[x][y - j])*(m.mask[start_h][start_w-j]))
               # R *=m.avg_k()
                resimg.picture[x][y] = R/(m.add_k())
        return resimg

    def SpaceFilter_notline(self,n,flag=0):  # 0- median  1- erosion   2- building up
        resimg=copy.deepcopy(self)

        if (flag == 0):
            m = Masks.Mask(n)
            m.fill_one()
            a=list()


            start_h = int((m.heigth - 1) / 2)
            start_w = int((m.width - 1) / 2)

            end_h = resimg.heigth - start_h
            end_w = resimg.width - start_w

            for x in range(start_h, end_h):
                for y in range(start_w, end_w):
                    a.clear()
                    for i in range(1,int((m.heigth+1) / 2)):
                        for j in range(1,int((m.width+1) / 2)):
                            if (m.mask[start_h + i][start_w + j]  !=0 ):
                                a.append(resimg.picture[x + i][y + j])
                            if (m.mask[start_h - i][start_w + j]  != 0):
                                a.append(resimg.picture[x - i][y + j])
                            if (m.mask[start_h + i][start_w - j]  != 0):
                                a.append(resimg.picture[x + i][y - j])
                            if (m.mask[start_h - i][start_w - j]  != 0):
                                a.append(resimg.picture[x - i][y - j])
                    a.append(resimg.picture[x][y])
                    for i in range(1,int((m.heigth + 1) / 2)):
                        a.append(resimg.picture[x+i][y])
                        a.append(resimg.picture[x-i][y])
                    for j in range(1,int((m.width + 1) / 2)):
                        a.append(resimg.picture[x][y+j])
                        a.append(resimg.picture[x][y-j])
                    a = sorted(a)
                    resimg.picture[x][y]=a[int((m.heigth*m.width)/2)]
        if (flag == 1):   # эрозия
             resimg=resimg.Filters_morf(n,0)
        if (flag == 2):   # наращивание
             resimg=resimg.Filters_morf(n,1)
        return resimg

    def SpaceFilter_laplacian(self,flag=0):     # 0 - без диагональных элементов   1 - с диагональными элементами
        resimg = copy.deepcopy(self)
        a = copy.deepcopy(self)

        m=Masks.Mask(3)

        if (flag ==0):
            m.fill_lap90()
        else:
            m.fill_lap45()

        # элементы проверки
        #m.print()
        #print(resimg.heigth,"x",resimg.width)

        laplacian = 0

        for i in range(1,resimg.heigth-1):
            for j in range(1,resimg.width-1):
                laplacian=0
                for n in range(3):
                    for m1 in range(3):
                        laplacian+=(m.mask[n][m1])*(a.picture[i-1+n][j-1+m1])
                resimg.picture[i][j] +=  laplacian

        return resimg

    def SpaceFilter_sobel(self):
        resimg = copy.deepcopy(self)
        a = copy.deepcopy(self)

        dx=0
        dy=0
        for i in range(1,resimg.heigth-1):
            for j in range(1,resimg.width-1):
                dx = 0
                dy = 0
                dx = mt.fabs((a.picture[i+1][j-1]+2*a.picture[i+1][j]+a.picture[i+1][j+1])-(a.picture[i-1][j-1]+2*a.picture[i-1][j]+a.picture[i-1][j+1]))
                dy = mt.fabs((a.picture[i - 1][j + 1] + 2 * a.picture[i ][j+1] + a.picture[i + 1][j + 1]) - (a.picture[i - 1][j - 1] + 2 * a.picture[i ][j-1] + a.picture[i + 1][j - 1]))
                resimg.picture[i][j]=dx+dy

        return resimg

    def Filters_morf(self,n=3,flag=0):      # falg == 0 - erosion (max), flag == 1 - наращивание (min)
        resimg=copy.deepcopy(self)
        A=copy.deepcopy(self)

        m=Masks.Mask(n)
        m.fill_one()

        start_h = int((m.heigth - 1) / 2)
        start_w = int((m.width - 1) / 2)

        end_h = resimg.heigth - start_h
        end_w = resimg.width - start_w

        a=list()

        for x in range(start_h, end_h):
            for y in range(start_w, end_w):
                a.clear()
                for i in range(1, int((m.heigth + 1) / 2)):
                    for j in range(1, int((m.width + 1) / 2)):
                        if (m.mask[start_h + i][start_w + j] != 0):
                            a.append(A.picture[x + i][y + j])
                        if (m.mask[start_h - i][start_w + j] != 0):
                            a.append(A.picture[x - i][y + j])
                        if (m.mask[start_h + i][start_w - j] != 0):
                            a.append(A.picture[x + i][y - j])
                        if (m.mask[start_h - i][start_w - j] != 0):
                            a.append(A.picture[x - i][y - j])
                a.append(A.picture[x][y])
                for i in range(1, int((m.heigth + 1) / 2)):
                    a.append(A.picture[x + i][y])
                    a.append(A.picture[x - i][y])
                for j in range(1, int((m.width + 1) / 2)):
                    a.append(A.picture[x][y + j])
                    a.append(A.picture[x][y - j])
                a = sorted(a)

                for i in range(m.heigth):
                    for j in range(m.width):
                        if (flag==0):  # erosion
                            if (A.picture[x-int((m.heigth - 1) / 2)+i][y-int((m.width - 1) / 2)+j]==max(a)):
                                for i1 in range(m.heigth):
                                    for j1 in range(m.width):
                                        resimg.picture[x - int((m.heigth - 1) / 2) + i1][y - int((m.width - 1) / 2) + j1] = max(a)
                        if (flag==1):  # наращивание
                            if (A.picture[x-int((m.heigth - 1) / 2)+i][y-int((m.width - 1) / 2)+j]==min(a)):
                                for i1 in range(m.heigth):
                                    for j1 in range(m.width):
                                        resimg.picture[x - int((m.heigth - 1) / 2) + i1][y - int((m.width - 1) / 2) + j1] = min(a)


        return resimg
