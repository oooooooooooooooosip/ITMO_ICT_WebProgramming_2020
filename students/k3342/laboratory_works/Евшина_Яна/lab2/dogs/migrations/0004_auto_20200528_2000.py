# Generated by Django 3.0.4 on 2020-05-28 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_auto_20200528_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dogs.Club'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='expert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='perform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dogs.Perform'),
        ),
        migrations.AlterField(
            model_name='ring',
            name='show',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dogs.Show'),
        ),
    ]
