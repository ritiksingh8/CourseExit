# Generated by Django 2.2.6 on 2020-09-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200710_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='batch',
            field=models.CharField(default='2020', max_length=4),
        ),
        migrations.AddField(
            model_name='course',
            name='sem_type',
            field=models.CharField(default='odd', max_length=4),
        ),
    ]
