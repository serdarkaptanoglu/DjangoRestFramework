# Generated by Django 5.1.4 on 2024-12-12 23:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=300, null=True)),
                ('sehir', models.CharField(blank=True, max_length=120, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiller',
            },
        ),
        migrations.CreateModel(
            name='ProfilDurum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durum_mesaji', models.CharField(max_length=150)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
                ('user_profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiller.profil')),
            ],
            options={
                'verbose_name_plural': 'Profil Mesajları',
            },
        ),
    ]
