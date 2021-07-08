# Generated by Django 2.2 on 2021-06-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210511_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='lotteryCount',
        ),
        migrations.AddField(
            model_name='profile',
            name='dailyScores',
            field=models.IntegerField(default=0, verbose_name='每日成绩'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dailyScoresRank',
            field=models.IntegerField(default=-1, verbose_name='每日成绩排名'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dailyUnitsNum',
            field=models.IntegerField(default=0, verbose_name='每日学习单元数'),
        ),
        migrations.AddField(
            model_name='profile',
            name='reviewCorrectRates',
            field=models.IntegerField(default=0, verbose_name='复习正确率'),
        ),
        migrations.AddField(
            model_name='profile',
            name='reviewCorrectRatesRank',
            field=models.IntegerField(default=-1, verbose_name='复习正确率排名'),
        ),
        migrations.AddField(
            model_name='profile',
            name='studyInfo',
            field=models.CharField(default='暂无', max_length=100, verbose_name='学习情况'),
        ),
        migrations.AddField(
            model_name='profile',
            name='studySuggestion',
            field=models.CharField(default='暂无', max_length=100, verbose_name='学习建议'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='暂无', max_length=20, verbose_name='昵称'),
        ),
    ]