# Generated by Django 3.0.5 on 2020-04-30 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_auto_20200430_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobile',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='driverlicense',
            options={'verbose_name': 'Водительское удостоверение', 'verbose_name_plural': 'Водительские удостоверения'},
        ),
        migrations.AlterModelOptions(
            name='owning',
            options={'verbose_name': 'Владение автомобилем'},
        ),
    ]
