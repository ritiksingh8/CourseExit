# Generated by Django 2.2.6 on 2020-07-10 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200710_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseexitstatus',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
