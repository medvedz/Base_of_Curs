import cv2 as cv
import numpy as np
import matplotlib as mp

BYTE = 256

<<<<<<< HEAD
=======

>>>>>>> 790a043706f7b19ed3d365c94ca815b275d5fcb9
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