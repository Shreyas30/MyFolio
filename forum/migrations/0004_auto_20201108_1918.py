# Generated by Django 3.1.2 on 2020-11-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20201108_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribeduser',
            name='portfolio',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
