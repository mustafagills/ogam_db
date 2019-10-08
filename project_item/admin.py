from django.contrib import admin
from .models import Proje, personel_yetkilendirme,proje_tip, proje_durum, proje_status

admin.site.register(Proje)
admin.site.register(proje_tip)
admin.site.register(proje_durum)
admin.site.register(proje_status)
# admin.site.register(proje_arsiv)
admin.site.register(personel_yetkilendirme)
# Register your models here.
