# Generated by Django 3.0.4 on 2020-04-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_importance',
            field=models.IntegerField(verbose_name='Важность (от 1 до 5)'),
        ),
    ]
