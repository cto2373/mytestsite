# Generated by Django 4.2.3 on 2023-07-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_movie_runtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starRating',
            field=models.CharField(max_length=50),
        ),
    ]