# Generated by Django 5.0.4 on 2024-05-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Majorsubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('durations', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'Major Subject',
            },
        ),
    ]