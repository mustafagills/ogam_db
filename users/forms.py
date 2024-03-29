from django import forms
from .models import User4Personels
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User4Personels
        fields = (
            'id',
            'ilkad',
            'soyad',
            'active',
            'unvan',
            'baslama_tarih',
            'bitis_tarih',
            'yetki_kod',
            'kullanici_tipi_no',
            'email',
            'kullanici_kod',
            'password',
            'admin',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User4Personels
        fields = (
            'id',
            'ilkad',
            'soyad',
            'active',
            'unvan',
            'baslama_tarih',
            'bitis_tarih',
            'yetki_kod',
            'kullanici_tipi_no',
            'email',
            'kullanici_kod',
            'password',
            'admin',
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget = forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User4Personels
        fields = (
            'id',
            'ilkad',
            'soyad',
            'unvan',
            'email',
            'yetki_kod',
            'kullanici_tipi_no',
            'kullanici_kod',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

        """personel_no integer not null ,
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
primary key (personel_no)  constraint personel_pk"""
