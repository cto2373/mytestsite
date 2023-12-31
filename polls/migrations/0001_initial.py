# Generated by Django 4.2.3 on 2023-07-08 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, verbose_name='Title')),
                ('starRating', models.DecimalField(decimal_places=0.0, default=0, max_digits=10.0)),
                ('rating', models.CharField(max_length=240, verbose_name='Rating')),
                ('year', models.TimeField(verbose_name='Years')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('runTime', models.DecimalField(decimal_places=0.2, default=0, max_digits=24.0)),
                ('cast', models.CharField(max_length=200, verbose_name='Cast')),
                ('iamge', models.CharField(max_length=512, verbose_name='Image')),
            ],
        ),
    ]
