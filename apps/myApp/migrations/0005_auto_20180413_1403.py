# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-13 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20180413_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='wishlist',
            field=models.ManyToManyField(related_name='wish_items', to='myApp.User'),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
