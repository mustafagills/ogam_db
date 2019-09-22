from django.db import models
from django.utils import timezone

class proje_tip(models.Model):
    proje_tip = models.IntegerField()
    aciklama = models.CharField(max_length= 50)
    id = models.AutoField(primary_key = True)

class proje_status(models.Model):
    proje_status_kod = models.IntegerField()
    aciklama = models.CharField(max_length = 20)
    id = models.AutoField(primary_key = True)

class proje_durum(models.Model):
    proje_durum = models.IntegerField()
    aciklama = models.CharField(max_length = 30)
    id = models.AutoField(primary_key = True)

class proje_arsiv:
    proje_kod = models.IntegerField()
    aciklama = models.CharField(max_length = 100)
    aciklama_date = models.DateTimeField()

class personel_yetkilendirme(models.Model):
    personel_no = models.IntegerField()
    proje_kod = models.IntegerField()
    yetki_kod = models.IntegerField()
    baslanma_tarih = models.DateTimeField()
    bitis_tarih = models.DateTimeField()
    id = models.AutoField(primary_key = True)

class Proje(models.Model): ## TODO: tekrar bak
    proje_kod = models.IntegerField()
    proje_adi = models.CharField(max_length = 140, verbose_name = 'proje adı')
    baslama_tarihi = models.DateTimeField()
    bitis_tarihi = models.DateTimeField()
    proje_yoneticisi = models.IntegerField()
    proje_teknik_yonetici_no = models.IntegerField()
    proje_calisanlar_no = models.TextField(default=False)
    aciklama = models.CharField(max_length = 100)
    """proje_durumu = models.ForeignKey(proje_durum, on_delete = models.CASCADE)
    proje_status = models.ForeignKey(proje_status, on_delete = models.CASCADE)
    proje_tip = models.ForeignKey(proje_tip, on_delete = models.CASCADE)"""

    def __str__(self):
        return self.proje_adi


# class Personel(models.Model):
#     active = models.BooleanField(default=False)
#     personel_pk = models.AutoField(primary_key = True)
#     personel_no = models.IntegerField(unique = True)
#     ilkad = models.CharField(max_length = 20)
#     soyad = models.CharField(max_length = 20)
#     baslama_tarih = models.DateTimeField()
#     bitis_tarih = models.DateTimeField()
#     yetki_kod = models.IntegerField()
#     kullanici_tipi_no = models.IntegerField()
#     e_mail = models.EmailField()
#     kullanici_kod = models.CharField(max_length = 11)
#
#     def __str__(self):
#         return self.ilkad + self.soyad

'''create table proje_tip
  (
    proje_tip integer not null ,
    aciklama char(50),
    primary key (proje_tip)  constraint prj_tip_pk
  )

create table proje_status
  (
    proje_status_kod integer not null,
    aciklama char(20),
    primary key (proje_status_kod)  constraint prj_status_kod_pk
  )
create table proje_durum
  (
    proje_durum integer,
    aciklama  char(30),
    primary key (proje_durum) constraint prj_dur_pk
  )
create table personel
  (
    personel_no integer not null ,
    ilkad char(20) not null,
    soyad char(20) not null,
    aktif_pasif integer, (1=aktif, 0=pasif)
    unvan integer,
    baslama_tarih date,
    bitis_tarih date,
    yetki_kod integer not null,
    kullanici_tipi_no integer not null ,
    e_mail char(50),
    kullanici_kod char(11)not null ,
    primary key (personel_no)  constraint personel_pk
  )

create table personel_yetkilendirme
  (
    personel_no integer not null ,
    proje_kod integer not null ,
    yetki_kod integer not null ,
    baslanma_tarih date not null ,
    bitis_tarih date not null ,
    primary key (personel_no,proje_kod,yetki_kod)  constraint yetki_pk
  )
create table proje
  (
    proje_kod integer not null,
    proje_adi char(50) not null ,
    baslama_tarihi date,
    bitis_tarihi date,
    proje_tip integer not null,
    proje_durum integer,
    proje_status_kod integer
    kullanici_kod char(11),
    personel_no integer not null,
    yetki_kod integer not null,
    kullanici_no integer not null,
    aciklama  char(100),
    primary key (proje_kod)  constraint proje_pk
  )


create table proje_arsiv
  (
    proje_kod integer not null ,
    aciklama char(100),
    aciklama_date date
    )'''
# Create your models here.
