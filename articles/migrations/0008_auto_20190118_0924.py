# Generated by Django 2.1.5 on 2019-01-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190118_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='_hook_rendered',
        ),
        migrations.AlterField(
            model_name='article',
            name='hook',
            field=models.TextField(),
        ),
    ]
