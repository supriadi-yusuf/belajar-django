# Generated by Django 2.0.3 on 2018-03-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0004_auto_20180327_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='kunci1',
        ),
        migrations.RemoveField(
            model_name='book',
            name='kunci2',
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
