import numpy as np

class Mask:

    def __init__(self,n):
        if (n<3):  n = 3                      # min size 3x3
        else:
            if (n%2==0): n-=1

        self.heigth=n                         
        self.width=n
        self.mask=np.zeros((n,n))
        
    def SetMaskSize(self,n):

        if (n<3): n=3                         #min size 3x3
        else:
            if (n%2==0): n-=1                 # если маска четного размера , то размер уменьшается на 1
                                              # , при этом он больше или равен 3

        self.heigth = n                       # size nxn
        self.width = n
        self.mask=np.zeros((n,n))


    def print(self): print(self.mask)          # print mask   
        
    def fill_one(self):                        # заполнить маску единицами
        for i in range(self.heigth):
            for j in range(self.width):
                self.mask[i][j]=1


    def fill_avg(self):                        # заполнить маску для взвешенного среднего
        self.fill_one()
        for i in range(1,int((self.width+1)/2)):
            self.mask[0][i]=self.mask[0][i-1] * 2
        for i in range(int((self.width+1)/2),self.width):
            self.mask[0][i]=self.mask[0][i-1] / 2

        for i in range(self.width):
            for j in range(1,int((self.heigth+1)/2)):
                self.mask[j][i]=self.mask[j-1][i]*2

        for i in range(self.width):
            for j in range(int((self.heigth/2)+1),self.heigth):
                self.mask[j][i] = self.mask[j - 1][i] / 2


    def add_k(self):                        # сумма коэф. маски
        k=0

        #if (self.mask[1][1]==self.mask[1][2]) :
        #   k=self.heigth*self.width
        #else:

        for i in range(int((self.width-1)/2)):
               for j in range(int((self.heigth+1)/2)):
                   k+=self.mask[j][i]
        k*=4
        k+=self.mask[int((self.heigth)/2)][int((self.width)/2)]
        return k

    def avg_k(self):                           # посчитать усредняющий коэф.
        return (float (1/self.add_k()))


