import numpy as np

class Mask:

    def __init__(self,n):
        n1=n
        if (n<3):  n1 = 3                      # min size 3x3
        else:
            if (n%2==0): n1=n-1

        self.heigth=n1
        self.width=n1
        self.mask=np.zeros((n1,n1))
        
    def SetMaskSize(self,n):
        n1=n
        if (n<3): n1=3                         #min size 3x3
        else:
            if (n%2==0): n1=n-1                 # если маска четного размера , то размер уменьшается на 1
                                              # , при этом он больше или равен 3

        self.heigth = n1                       # size nxn
        self.width = n1
        self.mask=np.zeros((n1,n1))


    def print(self): print(self.mask)          # print mask   
        
    def fill_one(self):                        # заполнить маску единицами
        for i in range(self.heigth):
            for j in range(self.width):
                self.mask[i][j]=1

    def fill_avg(self):                        # заполнить маску для взвешенного среднего
        """
        Маска заполняется степенями двойки , так как этот вариант проще в реализации
        при уже написанном методе заполнения маски единицами и дальнейшей работе
        по преобразованию ее коффициентов.

        Но чаще маску заполняют используя нормальное (Гауссово) распределение.

        """
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

    def fill_circle(self):                    # заполнить маску бинарным кружочком =)
        x=int(self.heigth/2)
        y=int(self.width/2)

        self.mask[x][y]=1

        for i in range(1,int((self.heigth)/2)+1):
            self.mask[x + i][y]=1
            self.mask[x - i][y]=1
        for j in range(1,int((self.width ) / 2)+1):
            self.mask[x ][y - j]=1
            self.mask[x ][y + j]=1

        for i in range(1,int(self.heigth/2)+1):
            j=1
            while (j<int(self.width/2)+1-i):
                self.mask[x + i][y + j] = 1
                self.mask[x - i][y + j] = 1
                self.mask[x + i][y - j] = 1
                self.mask[x - i][y - j] = 1
                j+=1

        if((self.heigth>5)and(self.width>5)):
            self.mask[self.heigth-1][int(self.width/2)] = 0
            self.mask[0][int(self.width / 2)] = 0
            self.mask[int(self.heigth/2)][0] = 0
            self.mask[int(self.heigth/2)][self.width - 1] = 0

    def add_k(self):                        # сумма коэф. маски
        #k=self.mask.sum()
        return self.mask.sum()

    def avg_k(self):                           # посчитать усредняющий коэф.
        return (float (1/self.add_k()))


