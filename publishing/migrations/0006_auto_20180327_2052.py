# Generated by Django 2.0.3 on 2018-03-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0005_auto_20180327_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        #migrations.AddField(
        #    model_name='book',
        #    name='id',
        #    field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        #    preserve_default=False,
        #),
    ]
