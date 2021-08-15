# Generated by Django 3.1.2 on 2020-11-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20201108_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='sender_fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='posts',
            name='sender_lname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='subscribeduser',
            name='portfolio',
            field=models.FileField(default='', upload_to='portfolio'),
        ),
    ]