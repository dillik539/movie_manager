# Generated by Django 2.0.4 on 2018-05-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_management_app', '0004_movierating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierating',
            name='rating',
            field=models.CharField(max_length=200),
        ),
    ]
