# Generated by Django 4.1.3 on 2022-12-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=50)),
                ('nombre_de_personaje', models.CharField(max_length=50)),
                ('espectativa_de_vida', models.IntegerField()),
                ('historia', models.URLField()),
            ],
        ),
    ]
