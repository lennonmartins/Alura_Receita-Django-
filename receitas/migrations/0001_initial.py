# Generated by Django 2.2.6 on 2022-12-18 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_receita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TimeField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
