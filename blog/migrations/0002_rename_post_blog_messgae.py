# Generated by Django 4.1.1 on 2022-09-11 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='post',
            new_name='messgae',
        ),
    ]