# Generated by Django 3.0.6 on 2020-05-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HKmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='block',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='task',
            field=models.TextField(),
        ),
    ]
