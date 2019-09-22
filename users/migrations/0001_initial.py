# Generated by Django 2.2.3 on 2019-09-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User4Personels',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(default=True, max_length=255, unique=True)),
                ('ilkad', models.CharField(max_length=20)),
                ('soyad', models.CharField(max_length=20)),
                ('unvan', models.IntegerField(blank=True, null=True)),
                ('yetki_kod', models.IntegerField()),
                ('baslama_tarih', models.DateTimeField(blank=True, null=True)),
                ('bitis_tarih', models.DateTimeField(blank=True, null=True)),
                ('kullanici_tipi_no', models.IntegerField()),
                ('kullanici_kod', models.CharField(max_length=11)),
                ('active', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
