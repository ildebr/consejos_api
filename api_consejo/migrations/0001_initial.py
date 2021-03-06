# Generated by Django 3.1.7 on 2022-03-17 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consejero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consejo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('U', 'Universitario'), ('A', 'Academico')], max_length=1)),
                ('meet_date', models.DateField()),
            ],
            options={
                'ordering': ('meet_date',),
            },
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciate', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('D', 'Decision'), ('I', 'Informacion')], max_length=1)),
                ('decision', models.CharField(choices=[('R', 'Rechazado'), ('D', 'Diferido')], max_length=1)),
                ('accordance', models.TextField(max_length=1000)),
                ('consejos_puntos', models.ManyToManyField(to='api_consejo.Consejo')),
                ('id_consejero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_consejo.consejero')),
            ],
        ),
        migrations.CreateModel(
            name='Instrucciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField(max_length=1000)),
                ('id_punto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_consejo.punto')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('route', models.CharField(max_length=100)),
                ('id_punto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_consejo.punto')),
            ],
        ),
        migrations.AddField(
            model_name='consejero',
            name='consejos_consejeros',
            field=models.ManyToManyField(to='api_consejo.Consejo'),
        ),
        migrations.AddField(
            model_name='consejero',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consejero', to=settings.AUTH_USER_MODEL),
        ),
    ]
