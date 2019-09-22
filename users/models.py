from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, ilkad, soyad, yetki_kod, kullanici_tipi_no, kullanici_kod,id, active = True, password = None):
        if not email or not ilkad or not soyad or not kullanici_tipi_no or not kullanici_kod or not yetki_kod:
            raise ValueError("E-mail, ilkad, soyad, yetki kodu, kullanıcı tipi no, kullanıcı kod, personel no alanları boş kalamaz.")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.id = id
        user_obj.ilkad, user_obj.soyad = ilkad, soyad
        user_obj.active = active
        user_obj.yetki_kod = yetki_kod
        user_obj.baslama_tarih = timezone.now
        user_obj.kullanici_tipi_no = kullanici_tipi_no
        user_obj.kullanici_kod = kullanici_kod
        user_obj.id = id
        user_obj.save(using=self._db)

        return user_obj


    def create_staffuser(self, email, ilkad, soyad, yetki_kod, kullanici_tipi_no, kullanici_kod,id, active = True, password = None):
        user = self.create_user(
            email,
            password=password,
            ilkad = ilkad,
            soyad = soyad,
            yetki_kod = yetki_kod,
            baslama_tarih = timezone.now,
            active = active,
            kullanici_tipi_no = kullanici_tipi_no,
            kullanici_kod = kullanici_kod,
            id = id,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, ilkad, soyad, yetki_kod,kullanici_tipi_no, kullanici_kod,id, active = True, password = None):
        user = self.create_user(
            email,
            password=password,
            ilkad = ilkad,
            soyad = soyad,
            yetki_kod = yetki_kod,
            baslama_tarih = timezone.now,
            active = active,
            kullanici_tipi_no = kullanici_tipi_no,
            kullanici_kod = kullanici_kod,
            id = id,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User4Personels(AbstractBaseUser):
    id = models.IntegerField(unique = True, blank = False, primary_key=True, verbose_name='Personel No')
    email = models.EmailField(unique=True, max_length = 255, default = True)
    ilkad = models.CharField(max_length = 20, blank = False)
    soyad = models.CharField(max_length = 20, blank = False)
    unvan = models.IntegerField(null = True, blank = True)
    yetki_kod = models.IntegerField(blank=False)
    baslama_tarih = models.DateTimeField(default=timezone.now)
    bitis_tarih = models.DateTimeField(null = True, blank = True)
    kullanici_tipi_no = models.IntegerField(blank = False)
    kullanici_kod = models.CharField(max_length = 11, blank = False)

    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'id',
        'ilkad',
        'soyad',
        'yetki_kod',
        'kullanici_tipi_no',
        'kullanici_kod',
    ]

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.ilkad + self.soyad

    def get_short_name(self):
        # The user is identified by their email address
        return self.ilkad

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

"""class AnotherUser(models.Model):
    user = models.OneToOneField(User4Personels)

    you CAN extend the user with extra data HERE. """



# Create your models here.

"""class Personel(models.Model):
    active_passive = [(1, 'Aktif'), (2, 'Pasif')]

    personel_pk = models.AutoField(primary_key = True)
    personel_no = models.IntegerField(unique = True)
    ilkad = models.CharField(max_length = 20)
    soyad = models.CharField(max_length = 20)
    aktif_pasif = models.IntegerField(choices = active_passive, verbose_name = 'Aktif/Pasif')
    unvan = models.IntegerField()
    baslama_tarih = models.DateTimeField()
    bitis_tarih = models.DateTimeField()
    yetki_kod = models.IntegerField()
    kullanici_tipi_no = models.IntegerField()
    e_mail = models.EmailField()
    kullanici_kod = models.CharField(max_length = 11)

    def __str__(self):
        return self.ilkad + self.soyad """

"""
create table personel(
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
  """
