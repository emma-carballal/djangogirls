# Generated by Django 3.2.25 on 2024-04-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_2',
            field=models.TextField(default='1234'),
            preserve_default=False,
        ),
    ]
