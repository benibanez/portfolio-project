# Generated by Django 2.2.6 on 2019-10-26 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobsConfig',
            new_name='Job',
        ),
    ]