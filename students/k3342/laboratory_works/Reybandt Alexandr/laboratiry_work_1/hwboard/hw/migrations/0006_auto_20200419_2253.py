# Generated by Django 3.0.4 on 2020-04-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0005_auto_20200419_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='teacher',
            field=models.CharField(max_length=150, verbose_name='Преподаватель'),
        ),
    ]
