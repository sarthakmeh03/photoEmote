# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.CharField(editable=False, max_length=10)),
                ('url', models.ImageField(upload_to=b'static/images')),
                ('created_at', models.DateTimeField(editable=False)),
                ('description', models.TextField()),
                ('orientation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_type', models.CharField(default=b'Like', max_length=20)),
                ('pixels', models.CharField(max_length=50)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoEmote.Image')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255)),
                ('user_id', models.CharField(editable=False, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoEmote.User'),
        ),
        migrations.AddField(
            model_name='image',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoEmote.User'),
        ),
    ]