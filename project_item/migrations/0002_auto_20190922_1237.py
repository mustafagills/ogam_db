# Generated by Django 2.2.3 on 2019-09-22 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='proje_teknik_yonetici_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
