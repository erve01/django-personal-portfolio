# Generated by Django 4.1.1 on 2022-09-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_date_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='message',
            field=models.TextField(),
        ),
    ]
