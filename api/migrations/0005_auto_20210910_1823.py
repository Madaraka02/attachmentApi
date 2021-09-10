# Generated by Django 3.2 on 2021-09-10 15:23

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210910_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='password',
            field=models.CharField(default=api.models.Company.company, max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='password',
            field=models.CharField(default=api.models.School.school, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default=api.models.Student.student, max_length=50),
        ),
    ]