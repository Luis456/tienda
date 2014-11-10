# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cliente', models.CharField(max_length=150)),
                ('fecha', models.DateField(auto_now=True)),
                ('Stock', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=150)),
                ('Descripcion', models.CharField(max_length=150)),
                ('precio', models.FloatField(default=0)),
                ('Stock', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pedido',
            name='Producto',
            field=models.ManyToManyField(to='Producto.Producto'),
            preserve_default=True,
        ),
    ]
