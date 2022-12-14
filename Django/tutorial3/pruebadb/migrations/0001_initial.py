# Generated by Django 4.1 on 2022-09-11 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fundacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('creador', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField(null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='pruebadb.empresa')),
                ('lenguaje', models.ManyToManyField(to='pruebadb.lenguaje')),
            ],
        ),
    ]
