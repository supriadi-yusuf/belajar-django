# Generated by Django 2.0.3 on 2018-03-27 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0008_auto_20180327_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
