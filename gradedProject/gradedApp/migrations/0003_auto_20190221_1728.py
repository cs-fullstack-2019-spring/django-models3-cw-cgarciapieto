# Generated by Django 2.2 on 2019-02-21 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradedApp', '0002_auto_20190221_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
    ]
