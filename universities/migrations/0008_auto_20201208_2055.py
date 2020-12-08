# Generated by Django 3.1.3 on 2020-12-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0007_auto_20201208_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]