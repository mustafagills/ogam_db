# Generated by Django 2.2.3 on 2019-09-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_item', '0006_auto_20190924_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='proje',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
    ]
