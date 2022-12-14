# Generated by Django 4.1.2 on 2022-10-13 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modelo', '0002_alter_modelo_nombre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('kilometraje', models.PositiveSmallIntegerField(verbose_name='Kilometraje')),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Modelo', to='modelo.modelo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
            },
        ),
    ]
