import cv2
import numpy as np
import matplotlib as mp

class Filters(object):
    def __init__(self):
        pass
class Filters(object, cv2):
    def __init__(self, _pict):
        self.picture = _pict
        self.heigth, self.width = _pict.shape

