# Generated by Django 4.1 on 2022-09-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='recomendado',
            field=models.BooleanField(default=True),
        ),
    ]
