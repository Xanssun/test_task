# Generated by Django 3.2.19 on 2023-06-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230629_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
