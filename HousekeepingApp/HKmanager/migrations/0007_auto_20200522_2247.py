# Generated by Django 3.0.6 on 2020-05-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HKmanager', '0006_auto_20200522_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bedroom',
            name='apartment',
        ),
        migrations.AddField(
            model_name='bedroom',
            name='apartment',
            field=models.ManyToManyField(to='HKmanager.apartment'),
        ),
    ]