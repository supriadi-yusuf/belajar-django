# Generated by Django 2.0.3 on 2018-04-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0016_author_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='foto',
            field=models.ImageField(default='pas_foto/default.jpg', upload_to='pas_foto'),
        ),
    ]
