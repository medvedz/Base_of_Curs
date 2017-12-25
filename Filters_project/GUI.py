import sys

import Filters               # наши фильтры
import cv2 as cv             # OpenCV

from PyQt5.QtWidgets import  QToolTip, QPushButton, QMainWindow    # добавили кнопки и всплывающие подсказки
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox     # окна , приложение, message box
from PyQt5.QtGui import QIcon                         # иконки
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont



class Main(QWidget):   # класс Main наследуется от класса QWidget



    def __init__(self):
        super().__init__()    # super() вызыввает конструктор родителя для конструктора наследника
        self.initUI()         # метод для GUI



    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))  # шрифт подсказки

        self.setWindowTitle('Обработка изображения')  # имя окна

        # габариты окна
        w_w=850
        w_h=780

        # все три метода унаследованы от QWidget
        self.setGeometry(0,0,w_w , w_h)      # 1 и 2 параметры - позиция окна
                                             # 3 и 4 - ширина и высота соответственно
                                             # он заменяет resize() и move()
        self.setWindowIcon(QIcon('Icon.png'))       # изменение иконки приложения




        # добавим кнопки
        """
        btn_ch_A = QPushButton('A', self)
        btn_ch_A.setToolTip('Выбрать изображение А')
        btn_ch_A.resize(100, 50)  #  размеры кнопки
        btn_ch_A.move(50, 70)

        btn_ch_B = QPushButton('B', self)
        btn_ch_B.setToolTip('Выбрать изображение B')
        btn_ch_B.resize(100, 50)  #  размеры кнопки
        btn_ch_B.move(170, 70)

        btn_ch_C = QPushButton('C', self)
        btn_ch_C.setToolTip('Выбрать изображение С')
        btn_ch_C.resize(100, 50)  # рекомендуемые размеры кнопки
        btn_ch_C.move(290, 70)
        """
        btn_st = QPushButton('Показать исходные изображения', self)
        btn_st.setToolTip('Вывести на экран изображения до применения фильтров')
        btn_st.resize(300, 50)  # размеры кнопки
        btn_st.move(int(w_w/2)-150, 70)

        # добавим кнопки для фильтров
        btn_line_1_3 = QPushButton('Линейный однородный фильтр 3x3', self)
        btn_line_1_3.setToolTip('Обработка изображений <b>линейным</b> сглаживающим <b>однородным</b> фильтром с маской 3 на 3 пикселя')
        btn_line_1_3.resize(250, 50)  # размеры кнопки
        btn_line_1_3.move(100, 200)

        btn_line_1_5 = QPushButton('Линейный однородный фильтр 5x5', self)
        btn_line_1_5.setToolTip('Обработка изображений <b>линейным</b> сглаживающим <b>однородным</b> фильтром с маской 5 на 5 пикселей')
        btn_line_1_5.resize(250, 50)  # размеры кнопки
        btn_line_1_5.move(500, 200)

        btn_line_avg_5 = QPushButton('Линейный фильтр 5x5 с маской взвешенного среднего', self)
        btn_line_avg_5.setToolTip('Обработка изображений <b>линейным</b> сглаживающим фильтром с маской <b>взвешенного среднего</b> 5 на 5 пикселей')
        btn_line_avg_5.resize(350, 50)  # размеры кнопки
        btn_line_avg_5.move(450, 270)

        btn_line_avg_3 = QPushButton('Линейный фильтр 3x3 с маской взвешенного среднего', self)
        btn_line_avg_3.setToolTip('Обработка изображений <b>линейным</b> сглаживающим фильтром с маской <b>взвешенного среднего</b> 3 на 3 пикселя')
        btn_line_avg_3.resize(350, 50)  # размеры кнопки
        btn_line_avg_3.move(50, 270)

        btn_mid_3 = QPushButton('Медианный фильтр 3x3', self)
        btn_mid_3.setToolTip('Обработка изображений <b>медианным</b> фильтром с маской 3 на 3 пикселя')
        btn_mid_3.resize(250, 50)  # размеры кнопки
        btn_mid_3.move(100, 340)

        btn_mid_5 = QPushButton('Медианный фильтр 5x5', self)
        btn_mid_5.setToolTip('Обработка изображений <b>медианным</b> фильтром с маской 5 на 5 пикселей')
        btn_mid_5.resize(250, 50)  # размеры кнопки
        btn_mid_5.move(500, 340)

        btn_avg_mid_3 = QPushButton('Линейный(взвешенного среднего) 3x3 + Медианный 3x3', self)
        btn_avg_mid_3.setToolTip('Обработка изображений <b>линейныйм фильтром с маской взвешенного среднего</b>, а затем <b>медианным</b> фильтром с масками 3 на 3 пикселя')
        btn_avg_mid_3.resize(350, 50)  # размеры кнопки
        btn_avg_mid_3.move(50, 410)

        btn_mid_avg_3 = QPushButton('Медианный 3x3 + Линейный(взвешенного среднего) 3x3', self)
        btn_mid_avg_3.setToolTip('Обработка изображений <b>медианным</b> фильтром, а затем <b>линейныйм фильтром с маской взвешенного среднего</b> с масками 3 на 3 пикселя')
        btn_mid_avg_3.resize(350, 50)  # размеры кнопки
        btn_mid_avg_3.move(450, 410)

        btn_lap_90 = QPushButton('Повышение резкости (лапласиан 90)', self)
        btn_lap_90.setToolTip('Повышение рекости с помощью <b>лапласиана без диагональных элементов</b>')
        btn_lap_90.resize(350, 50)  # размеры кнопки
        btn_lap_90.move(50, 480)

        btn_lap_45 = QPushButton('Повышение резкости (лапласиан 45)', self)
        btn_lap_45.setToolTip('Повышение рекости с помощью <b>лапласиана c диагональными элементами</b>')
        btn_lap_45.resize(350, 50)  # размеры кнопки
        btn_lap_45.move(450, 480)

        btn_sobel = QPushButton('Фильтр Собеля', self)
        btn_sobel.setToolTip('Выделение <b>контуров</b> на изображении с помощью <b>градиентов</b>')
        btn_sobel.resize(350, 50)  # размеры кнопки
        btn_sobel.move(50, 550)

        btn_mid_sobel = QPushButton('Медианный + Фильтр Собеля', self)
        btn_mid_sobel.setToolTip('<b>Медианный 5x5</b> + выделение контуров <b>фильтром Собеля</b>')
        btn_mid_sobel.resize(350, 50)  # размеры кнопки
        btn_mid_sobel.move(450, 550)

        btn_mid_lap = QPushButton('Медианный + Повышение резкости', self)
        btn_mid_lap.setToolTip('<b>Медианный 3 на 3</b> + <b>Лапласиан</b> с диагональными элементами')
        btn_mid_lap.resize(350, 50)  # размеры кнопки
        btn_mid_lap.move(int(w_w/2)-175, 620)


        # добавим кнопку выхода
        ext=QPushButton('Выход',self)
        ext.setToolTip('Выход из приложения')
        ext.clicked.connect(QCoreApplication.instance().quit)
        ext.resize(100,50)
        ext.move(w_w-120,w_h-80)


        # сигналы нажатий на кнопки
        """
        #btn_ch_A.clicked.connect(self.button_ch_A_Clicked)
        #btn_ch_B.clicked.connect(self.button_ch_B_Clicked)
        #btn_ch_C.clicked.connect(self.button_ch_C_Clicked)
        """

        btn_st.clicked.connect(self.button_st_Clicked)

        btn_line_1_3.clicked.connect(self.button_line_1_3_Clicked)
        btn_line_1_5.clicked.connect(self.button_line_1_5_Clicked)

        btn_line_avg_5.clicked.connect(self.button_line_avg_5_Clicked)
        btn_line_avg_3.clicked.connect(self.button_line_avg_3_Clicked)

        btn_mid_3.clicked.connect(self.button_mid_3_Clicked)
        btn_mid_5.clicked.connect(self.button_mid_5_Clicked)

        btn_avg_mid_3.clicked.connect(self.button_avg_mid_3_Clicked)
        btn_mid_avg_3.clicked.connect(self.button_mid_avg_3_Clicked)

        btn_lap_90.clicked.connect(self.button_lap_90_Clicked)
        btn_lap_45.clicked.connect(self.button_lap_45_Clicked)
        btn_sobel.clicked.connect(self.button_sobel_Clicked)
        btn_mid_sobel.clicked.connect(self.button_mid_sobel_Clicked)
        btn_mid_lap.clicked.connect(self.button_mid_lap_Clicked)

        self.show()

    """
    def button_ch_A_Clicked(self):
        cv.imshow('A', A.picture)
        k=1

    def button_ch_B_Clicked(self):
        cv.imshow('B', B.picture)
        k=2

    def button_ch_C_Clicked(self):
        cv.imshow('C', C.picture)
        k=3
    """

    def button_mid_lap_Clicked(self):
        cv.imshow('D median 3x3 + lap 45', D.SpaceFilter_notline(3).SpaceFilter_laplacian(1).picture)

    def button_lap_90_Clicked(self):
        cv.imshow('D laplacian 90', D.SpaceFilter_laplacian().picture)

    def button_lap_45_Clicked(self):
        cv.imshow('D laplacian 45', D.SpaceFilter_laplacian(1).picture)

    def button_sobel_Clicked(self):
        cv.imshow('D sobel', D.SpaceFilter_sobel().picture)

    def button_mid_sobel_Clicked(self):
        cv.imshow('D median (5x5) + sobel', D.SpaceFilter_notline(5).SpaceFilter_sobel().picture)

    def button_line_1_5_Clicked(self):
        cv.imshow('A Line Filter (1) 5x5', A.SpaceFilter_line(5).picture)
        cv.imshow('B Line Filter (1) 5x5', B.SpaceFilter_line(5).picture)
        cv.imshow('C Line Filter (1) 5x5', C.SpaceFilter_line(5).picture)

    def button_line_1_3_Clicked(self):
        cv.imshow('A Line Filter (1) 3x3', A.SpaceFilter_line(3).picture)
        cv.imshow('B Line Filter (1) 3x3', B.SpaceFilter_line(3).picture)
        cv.imshow('C Line Filter (1) 3x3', C.SpaceFilter_line(3).picture)

    def button_line_avg_3_Clicked(self):
        cv.imshow('A Line Filter (avg) 3x3', A.SpaceFilter_line(3, 1).picture)
        cv.imshow('B Line Filter (avg) 3x3', B.SpaceFilter_line(3, 1).picture)
        cv.imshow('C Line Filter (avg) 3x3', C.SpaceFilter_line(3, 1).picture)

    def button_line_avg_5_Clicked(self):
        cv.imshow('A Line Filter (avg) 5x5', A.SpaceFilter_line(5, 1).picture)
        cv.imshow('B Line Filter (avg) 5x5', B.SpaceFilter_line(5, 1).picture)
        cv.imshow('C Line Filter (avg) 5x5', C.SpaceFilter_line(5, 1).picture)

    def button_mid_3_Clicked(self):
        cv.imshow('A median 3x3', A.SpaceFilter_notline(3).picture)
        cv.imshow('B median 3x3', B.SpaceFilter_notline(3).picture)
        cv.imshow('C median 3x3', C.SpaceFilter_notline(3).picture)

    def button_mid_5_Clicked(self):
        cv.imshow('A median 5x5', A.SpaceFilter_notline(5).picture)
        cv.imshow('B median 5x5', B.SpaceFilter_notline(5).picture)
        cv.imshow('C median 5x5', C.SpaceFilter_notline(5).picture)
        cv.imshow('C median 7x7', C.SpaceFilter_notline(7).picture)


    def button_avg_mid_3_Clicked(self):
        cv.imshow('A avg  + median', A.SpaceFilter_line(3, 1).SpaceFilter_notline(3).picture)
        cv.imshow('B avg  + median', B.SpaceFilter_line(3, 1).SpaceFilter_notline(3).picture)
        cv.imshow('C avg  + median', C.SpaceFilter_line(3, 1).SpaceFilter_notline(3).picture)

    def button_mid_avg_3_Clicked(self):
        cv.imshow('A median + avg', A.SpaceFilter_notline(3).SpaceFilter_line(3, 1).picture)
        cv.imshow('B median + avg', B.SpaceFilter_notline(3).SpaceFilter_line(3, 1).picture)
        cv.imshow('C median + avg', C.SpaceFilter_notline(3).SpaceFilter_line(3, 1).picture)

    def button_st_Clicked(self):
        cv.imshow('A', A.picture)
        cv.imshow('B', B.picture)
        cv.imshow('C', C.picture)
        cv.imshow('D', D.picture)


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход',
                                     "Вы уверены, что хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    B = Filters.Filters(cv.imread('test_img/7_black.png', cv.IMREAD_GRAYSCALE))
    A = Filters.Filters(cv.imread('test_img/test.png', cv.IMREAD_GRAYSCALE))
    C = Filters.Filters(cv.imread('test_img/1.png', cv.IMREAD_GRAYSCALE))
    D = Filters.Filters(cv.imread('test_img/lap.png', cv.IMREAD_GRAYSCALE))

    app = QApplication(sys.argv)   # создали приложение
    ex = Main()                 # создали окно
    ex.center()
    sys.exit(app.exec_())          # запуск основного цикла