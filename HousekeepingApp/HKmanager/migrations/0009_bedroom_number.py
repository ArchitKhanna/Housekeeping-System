# Generated by Django 3.0.6 on 2020-05-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HKmanager', '0008_auto_20200522_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedroom',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
