# Generated by Django 3.0.6 on 2020-05-17 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_auto_20200517_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentoffer',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitment.Category'),
        ),
    ]
