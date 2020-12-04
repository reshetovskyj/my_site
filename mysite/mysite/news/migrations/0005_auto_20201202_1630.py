# Generated by Django 3.1.3 on 2020-12-02 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201129_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категорія'),
            preserve_default=False,
        ),
    ]
