from ders02 import Ogretmen, Ders, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///okul_sistemi.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

ogretmenler = session.query(Ogretmen).all()

print(["{} öğretmeni {} Hoca".format(ders.isim+str(ders.ogretmen.yas), ogretmen.isim) for ogretmen in ogretmenler for ders in ogretmen.ders])

hasan = session.query(Ogretmen).filter(Ogretmen.isim == 'Hasan').first()
dersler = session.query(Ders).filter(Ders.ogretmen == hasan).all()
print("Hasan hocaya ait derler")
print([ders.isim for ders in dersler])