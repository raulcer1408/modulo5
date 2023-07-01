# Generated by Django 4.2.2 on 2023-06-26 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0004_curso_materia'),
    ]

    operations = [
        migrations.CreateModel(
            name='notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('tipo', models.CharField(max_length=50)),
                ('curs_mat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursomateria', to='notas.curso_materia')),
                ('est_gest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gestionest', to='notas.estudiante_gestion')),
            ],
        ),
    ]
