# Generated by Django 3.2.2 on 2021-05-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Techno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=250, null=True)),
                ('url_project', models.CharField(max_length=250)),
                ('url_git', models.CharField(max_length=250)),
                ('techno', models.ManyToManyField(to='portfolio.Techno')),
            ],
        ),
    ]
