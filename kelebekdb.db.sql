BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "dagitim_listeleri" (
	"dagitim_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"dagitim_adi"	TEXT,
	"dagitim_tarihi"	TEXT,
	"sinif_listesi"	TEXT,
	"fsinif_listesi"	TEXT,
	"toplu_liste"	TEXT
);
CREATE TABLE IF NOT EXISTS "ogrenci_listesi" (
	"ogrenci_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"ogrenci_no"	INTEGER UNIQUE,
	"ogrenci_adi"	TEXT,
	"sube_bilgisi"	INTEGER
);
CREATE TABLE IF NOT EXISTS "fiziki_sinif" (
	"fsinif_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fsinif_adi"	TEXT UNIQUE,
	"fsinif_mevcut"	INTEGER
);
CREATE TABLE IF NOT EXISTS "sube_bilgileri" (
	"sube_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"sube_adi"	TEXT UNIQUE,
	"sube_mevcut"	INTEGER,
	"sube_ogrenci"	TEXT
);
CREATE TABLE IF NOT EXISTS "okul_bilgileri" (
	"kurum_kodu"	INTEGER UNIQUE,
	"kurum_adi"	TEXT,
	"kurum_sifre"	TEXT,
	"sube_sayisi"	INTEGER,
	PRIMARY KEY("kurum_kodu")
);
INSERT INTO "okul_bilgileri" VALUES (45454,'torbalı','789',12);
COMMIT;
