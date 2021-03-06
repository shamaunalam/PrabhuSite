# Generated by Django 2.2.6 on 2020-12-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=50)),
                ('TagLine1', models.CharField(max_length=50)),
                ('TagLine2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_desc', models.CharField(max_length=500)),
                ('Market_Analysis_desc', models.CharField(max_length=500)),
                ('Fast_Support_Desc', models.CharField(max_length=500)),
                ('Agents', models.CharField(max_length=500)),
            ],
        ),
    ]
