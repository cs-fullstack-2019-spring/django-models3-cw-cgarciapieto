# Generated by Django 2.2 on 2019-02-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pageNumber', models.IntegerField(max_length=10000)),
                ('genre', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.DateField()),
            ],
        ),
    ]
