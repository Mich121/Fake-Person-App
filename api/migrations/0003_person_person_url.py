# Generated by Django 3.1.7 on 2021-10-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211005_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_url',
            field=models.URLField(default='', unique=True),
        ),
    ]