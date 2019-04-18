# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subebilgileriguncelleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from db_islemleri import * #db işlemleri sayfasını aldık


class Sube_bilgi_guncelle(QtWidgets.QWidget):
    def __init__(self):
        super(Sube_bilgi_guncelle,self).__init__()

        self.setObjectName("Form")
        self.resize(623, 355)

        self.query = session.query(SubeBilgileri)
        self.tablo = QtWidgets.QTableWidget(self)
        self.tablo.setGeometry(QtCore.QRect(50,30,320,250))
        self.tablo.setRowCount(self.query.count()*2)
        self.tablo.setColumnCount(1)
        self.tablo.setHorizontalHeaderLabels(["Şube Adı Eski"])
        self.tablo.setColumnWidth(0, 300)
        a=0
        satirlar = []
        for dd in range(self.query.count()):
            print(dd)
            icerik = self.query.filter(SubeBilgileri.sube_id == dd + 1).first()
            self.tablo.setItem(dd,0,QtWidgets.QTableWidgetItem(icerik.sube_adi))

        self.guncelle = QtWidgets.QPushButton(self)
        self.guncelle.setGeometry(QtCore.QRect(530, 320, 75, 23))
        self.guncelle.setObjectName("guncelle")
        self.renciListesiEkLabel = QtWidgets.QLabel(self)
        self.renciListesiEkLabel.setGeometry(QtCore.QRect(400, 280, 90, 22))
        self.renciListesiEkLabel.setObjectName("renciListesiEkLabel")
        self.listeal = QtWidgets.QPushButton(self)
        self.listeal.setGeometry(QtCore.QRect(500, 280, 110, 23))
        self.listeal.setObjectName("listeal")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Şube bilgileri Güncelleme"))
        # self.subeadie1.setText(_translate("Form", "Şube Adı Giriniz"))
        self.guncelle.setText(_translate("Form", "Güncelle"))
        self.renciListesiEkLabel.setText(_translate("Form", "Öğrenci Listesi Çek"))
        self.listeal.setText(_translate("Form", "Listeyi Al"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Sube_bilgi_guncelle()
    ui.show()
    sys.exit(app.exec_())

