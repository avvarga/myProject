# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-13 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20180413_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wishlists',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='item',
            field=models.ManyToManyField(related_name='wishlisted', to='myApp.Item'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myApp.User'),
        ),
    ]
