# Generated by Django 2.2.3 on 2019-09-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190922_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user4personels',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Personel No'),
        ),
    ]