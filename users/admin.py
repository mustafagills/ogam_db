from django.contrib import admin
from .models import User4Personels
from. forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'personel_no']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['ilkad','soyad','personel_no','admin']
    list_filter = ['kullanici_tipi_no']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('ilkad', 'soyad')}),
        ('Kurumsal Bilgiler', {'fields': ('personel_no','unvan','yetki_kod','baslama_tarih','bitis_tarih','kullanici_kod', 'kullanici_tipi_no')}),
        ('İzinler', {'fields': ('active','admin','staff')}),
    )
    ordering = ['ilkad',]




admin.site.register(User4Personels, UserAdmin)
# Register your models here.
