# Generated by Django 2.0.3 on 2018-04-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0017_auto_20180404_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='logo',
            field=models.ImageField(default='simbol/deafult.jpg', upload_to='simbol'),
        ),
    ]
