# Generated by Django 4.1.3 on 2022-11-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='question'),
            preserve_default=False,
        ),
    ]