# Generated by Django 2.2 on 2021-06-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210621_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Grades',
            field=models.CharField(default='暂无', max_length=5, verbose_name='学习评级'),
        ),
    ]
