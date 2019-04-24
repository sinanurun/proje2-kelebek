# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yenidagitim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from ydagitim_ui import *
import sys
from db_islemleri import * #db işlemleri sayfasını aldık

class Yeni_Datigim(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.sinav_adi.textChanged.connect(self.deneme)
        self.sinav_sayisi.valueChanged.connect(self.tablo_olustur01)
        self.sinav_tablosu_01.setRowCount(1)
        self.sinav_tablosu_01.setItem(0, 0, QtWidgets.QTableWidgetItem(str(1) + ". Sınav Adı :"))
        self.sinav_tablosu_01.setItem(0, 1, QtWidgets.QTableWidgetItem("Sınav Adı Giriniz 01"))

        # self.sube_bilgileri.connect(self.tablo_olustur02)
        self.tab_bilgialanlari.currentChanged.connect(self.secim)

    def secim(self):
        self.alan = self.sender()
        self.secili_alan = self.alan.currentIndex()
        if self.secili_alan == 0:
            pass
        elif self.secili_alan == 1 :
            return self.tablo_olustur02()
        elif self.secili_alan == 2:
            return self.tablo_olustur03()


    def tablo_olustur01(self):
        self.gelen = self.sender()
        self.sinav_tablosu_01.setRowCount(int(self.gelen.text()))
        for dd in range(int(self.gelen.text())):
           self.sinav_tablosu_01.setItem(dd, 0, QtWidgets.QTableWidgetItem(str(dd+1)+". Sınav Adı :"))
           self.sinav_tablosu_01.setItem(dd, 1, QtWidgets.QTableWidgetItem("Sınav Adı Giriniz "+str(dd+1)))

    def tablo_olustur02(self):
        self.sinav_tablosu_02.setColumnCount(self.sinav_sayisi.value()+1)
        ders=[self.sinav_tablosu_02.horizontalHeaderItem(0).text()]
        for dd in range(self.sinav_sayisi.value()):
            ders.append(self.sinav_tablosu_01.item(dd,1).text())
        self.sinav_tablosu_02.setHorizontalHeaderLabels(ders)

        print(ders)

    def tablo_olustur03(self):
        print("sınav yerleri")

app = QtWidgets.QApplication(sys.argv)
giris = Yeni_Datigim()

giris.show()
sys.exit(app.exec_())