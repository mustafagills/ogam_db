from django.contrib import admin
from .models import User4Personels
from. forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'id']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['ilkad','soyad','id','admin']
    list_filter = ['kullanici_tipi_no']
    fieldsets = (
        (None, {
            'fields': (
                'id',
                'email',
                'password'
            )
        }),
        ('Kişisel Bilgiler', {
            'fields': (
                'ilkad',
                'soyad'
            )
        }),
        ('Kurumsal Bilgiler', {
            'fields': (
                'unvan',
                'yetki_kod',
                'baslama_tarih',
                'bitis_tarih',
                'kullanici_kod',
                'kullanici_tipi_no'
            )
        }),
        ('İzinler', {
            'fields': (
                'active',
                'admin',
                'staff'
            )
        }),
    )
    ordering = ['ilkad',]




admin.site.register(User4Personels, UserAdmin)
# Register your models here.
