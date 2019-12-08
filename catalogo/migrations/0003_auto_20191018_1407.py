# Generated by Django 2.2.6 on 2019-10-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20191018_1317'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('f', 'Femenino'), ('M', 'Masculino')], default='f', help_text='Seleccione Genero', max_length=1),
        ),
    ]
