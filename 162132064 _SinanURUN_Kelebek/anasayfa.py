from ansayfa_ui import Ui_Anaekran
from kurum_bilgileri_guncelleme_ui import *
from kurum_bilgileri import *


class Anapencere(QMainWindow,Ui_Anaekran):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.show()
        self.OkulBilgileriGuncelle.triggered.connect(self.obg)
        # self.SubeisimleriGuncelle.triggered.connect(self.sbg)
        # self.SubeListesi.triggered.connect(self.sl)
        # self.SinavyeriGuncelle.triggered.connect(self.syg)
        # self.KapasiteGuncelle.triggered.connect(self.kg)
        # self.YeniDagitim.triggered.connect(self.yd)
        # self.EskiDagitimlar.triggered.connect(self.ed)


     #okul bilgilerinin güncellenme sayfası ve işlemleri
    def obg(self):
        self.obgekrani = Kurumbg()
        self.setCentralWidget(self.obgekrani)
    def sbg(self):
        pass
    def sl(self):
        pass
    def syg(self):
        pass
    def kg(self):
        pass
    def yd(self):
        pass
    def ed(self):
        pass

