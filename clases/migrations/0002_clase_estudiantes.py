# Generated by Django 2.2.24 on 2021-11-10 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='estudiantes',
            field=models.ManyToManyField(related_name='Clases', to='estudiantes.Estudiante'),
        ),
    ]
