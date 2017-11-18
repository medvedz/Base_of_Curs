import cv2
import numpy as np
import matplotlib as mp


class Filters(object, cv2):
    def __init__(self, _pict):
        self.picture = _pict
        self.heigth, self.width = _pict.shape

    def GetHistogram(self):
        self.histogram = [0 for i in range(255)]
        for row in range(self.height):
            for col in range(self.width):
                self.histogram[self.picture[row, col]] += 1
        return self.histogram
