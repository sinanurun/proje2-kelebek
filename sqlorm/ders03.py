from ders02 import Ogretmen, Ders, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///okul_sistemi.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

hasan = Ogretmen(isim='Hasan',yas=25)
session.add(hasan)
ayse = Ogretmen(isim='Ayşe',yas=30)
session.add(ayse)
session.commit()

tarih = Ders(isim='Tarih', ogretmen=hasan)
cografya = Ders(isim='Cografya', ogretmen=hasan)
biyoloji = Ders(isim='Biyoloji', ogretmen=ayse)
fizik = Ders(isim='Fizik', ogretmen=ayse)

session.add_all([tarih, cografya, biyoloji, fizik])
session.commit()