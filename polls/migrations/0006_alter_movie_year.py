# Generated by Django 4.2.3 on 2023-07-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateTimeField(verbose_name='Years'),
        ),
    ]
