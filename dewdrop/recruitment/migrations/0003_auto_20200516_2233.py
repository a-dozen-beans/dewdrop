# Generated by Django 3.0.6 on 2020-05-16 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20200516_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='pub_date',
            new_name='join_date',
        ),
    ]
