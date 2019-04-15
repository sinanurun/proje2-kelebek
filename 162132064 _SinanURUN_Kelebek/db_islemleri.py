from orm_db import *


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def kurum_girisi(kkodu,sifre):
    print(kkodu,sifre)
    kgirisi = session.query(Kurum).filter(Kurum.kurum_kodu == kkodu, Kurum.kurum_sifre == sifre).first()
    try:
        if (kgirisi.kurum_adi) :
            print(kgirisi.kurum_adi)
            return True
    except:
        return False
    # if (kadi == kurum.kurum_kodu and kurum.kurum_sifre == sifre):
    #     print("doğru")
    # else:
    #     print("hatalı")

        #print(["{} öğretmeni {} Hoca".format(ders.isim+str(ders.ogretmen.yas), ogretmen.isim) for ogretmen in ogretmenler for ders in ogretmen.ders])

def kurumbilgileri():
    return session.query(Kurum).first()


def kgb_guncelle(*bilgiler):

    print(bilgiler)
    

    try:
        session.query(Kurum).filter(Kurum.kurum_kodu==123456).update(bilgiler, synchronize_session=False)
        session.commit()
    except:
        print("hata")

