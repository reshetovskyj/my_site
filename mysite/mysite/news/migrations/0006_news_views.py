# Generated by Django 3.1.3 on 2020-12-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201202_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
