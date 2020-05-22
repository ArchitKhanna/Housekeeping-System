# Generated by Django 3.0.6 on 2020-05-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HKmanager', '0003_auto_20200520_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='bedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='livingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='ensuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.apartment')),
                ('bedroom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.bedroom')),
            ],
        ),
        migrations.CreateModel(
            name='corridor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HKmanager.apartment')),
            ],
        ),
    ]
