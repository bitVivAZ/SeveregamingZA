# Generated by Django 2.1.5 on 2019-01-11 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Matches',
            new_name='Match',
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'Matches'},
        ),
    ]