# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_key', models.ForeignKey(to='shoppinglistdata.ShoppingList')),
                ('user_key', models.ForeignKey(to='shoppinglistdata.User')),
            ],
        ),
        migrations.AddField(
            model_name='itemlist',
            name='item_key',
            field=models.ForeignKey(to='shoppinglistdata.ShoppingItem'),
        ),
        migrations.AddField(
            model_name='itemlist',
            name='list_key',
            field=models.ForeignKey(to='shoppinglistdata.ShoppingList'),
        ),
        migrations.AddField(
            model_name='itemlist',
            name='user_key',
            field=models.ForeignKey(to='shoppinglistdata.User'),
        ),
    ]
