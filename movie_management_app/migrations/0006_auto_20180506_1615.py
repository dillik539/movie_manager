# Generated by Django 2.0.4 on 2018-05-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_management_app', '0005_auto_20180506_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierating',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
