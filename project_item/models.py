from django.db import models
from django.utils import timezone

class proje_tip(models.Model):
    proje_tip = models.IntegerField(primary_key=True)
    aciklama = models.CharField(max_length= 50)

    class Meta:
        verbose_name = 'Proje Tipi'
        verbose_name_plural = 'Proje Tipleri'

    def __str__(self):
        return str(self.proje_tip)
class proje_status(models.Model):
    proje_status_kod = models.IntegerField(primary_key=True)
    aciklama = models.CharField(max_length = 20)

    class Meta:
        verbose_name = 'Proje Status'
        verbose_name_plural = 'Proje Statusleri'

    def __str__(self):
        return str(self.proje_status_kod)

class proje_durum(models.Model):
    proje_durum = models.IntegerField(primary_key=True)
    aciklama = models.CharField(max_length = 30)

    class Meta:
        verbose_name = 'Proje Durum'
        verbose_name_plural = 'Proje Durumları'

    def __str__(self):
        return str(self.proje_durum)

# class proje_arsiv(models.Model):
#     proje_kod = models.IntegerField()
#     aciklama = models.CharField(max_length = 100, null=True, blank=True)
#     aciklama_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Proje Arşiv'
#         verbose_name_plural = 'Proje Arşiv'
#
#     def __str__(self):
#         return str(self.proje_kod)

class personel_yetkilendirme(models.Model):
    personel_no = models.ForeignKey('users.User4Personels', on_delete=models.CASCADE, related_name= "+", verbose_name='Personel No',null=True)
    proje_kod = models.ForeignKey('Proje', on_delete=models.CASCADE, related_name= "+", verbose_name='Proje Kod',null=True)
    yetki_kod = models.IntegerField(unique=True)
    baslanma_tarih = models.DateTimeField(null=True, blank=True)
    bitis_tarih = models.DateTimeField(null=True, blank=True)
    id = models.AutoField(primary_key = True)

    class Meta:
        verbose_name = 'Proje Yetkilendirme'
        verbose_name_plural = 'Proje Yetkilendirme'

    def __str__(self):
        return str(self.yetki_kod)

class Proje(models.Model):
    choices=[
                (1, 'Arşilendi'),
                (0, 'Arşivlenmedi')
            ]
    proje_kod = models.IntegerField(primary_key=True, verbose_name='Proje Kodu') #proje kodu
    proje_adi = models.CharField(max_length = 140, verbose_name = 'Proje Adı')
    baslama_tarihi = models.DateTimeField(verbose_name='Başlama Tarihi')
    bitis_tarihi = models.DateTimeField(verbose_name='Bitiş Tarihi',null=True, blank=True)
    proje_yoneticisi = models.ForeignKey('users.User4Personels', on_delete=models.CASCADE, related_name= "+", verbose_name='Proje Yöneticisi',null=True, blank=True)
    proje_teknik_yonetici_no = models.ForeignKey('users.User4Personels', on_delete=models.CASCADE, related_name= "+", verbose_name ='Proje Teknik Yönetici No',null=True, blank=True)
    proje_calisanlar_no = models.TextField(null=True,blank=True, verbose_name='Proje Çalışanlarının Numaraları')
    aciklama = models.CharField(max_length = 100, verbose_name='Açıklama', null=True, blank=True)
    proje_durumu = models.ForeignKey('proje_durum', on_delete=models.CASCADE,related_name= "+",null=True, blank=True, verbose_name='Proje Durumu')
    proje_status = models.ForeignKey('proje_status', on_delete=models.CASCADE,related_name= "+",null=True, blank=True, verbose_name='Proje Status')
    proje_tip = models.ForeignKey('proje_tip', on_delete=models.CASCADE,related_name= "+",null=True, blank=True, verbose_name='Proje Tipi')
    is_archive = models.IntegerField(choices=choices, default=0, verbose_name='Arşiv durumu')
    aciklama_date = models.DateTimeField(null=True, blank=True, verbose_name='Açıklama Tarihi(Yalnızca arşivlerken ekleyin.)')

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return str(self.proje_kod)

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
