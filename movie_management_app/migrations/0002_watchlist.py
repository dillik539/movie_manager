# Generated by Django 2.0.4 on 2018-05-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('actor', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
            ],
        ),
    ]