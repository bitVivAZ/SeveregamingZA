# Generated by Django 2.1.5 on 2019-01-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severe_team', models.CharField(max_length=50)),
                ('opponent', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=4)),
                ('match_result', models.CharField(max_length=10)),
                ('leg', models.CharField(max_length=10)),
                ('match_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='full name')),
            ],
        ),
    ]
