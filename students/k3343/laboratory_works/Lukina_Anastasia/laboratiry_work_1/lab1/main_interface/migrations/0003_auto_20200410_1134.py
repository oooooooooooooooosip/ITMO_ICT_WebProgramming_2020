# Generated by Django 2.1.5 on 2020-04-10 11:34

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main_interface', '0002_auto_20200410_1133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Themes',
            new_name='Theme',
        ),
    ]
