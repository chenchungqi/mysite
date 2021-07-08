from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, verbose_name='昵称', default='暂无')
    Grades = models.CharField(max_length=5, verbose_name='学习评级', default='暂无')
    dailyScores = models.IntegerField(verbose_name='每日成绩', default=0)
    dailyScoresRank = models.IntegerField(verbose_name='每日成绩排名', default=-1)
    dailyUnitsNum = models.IntegerField(verbose_name='每日学习单元数', default=0)
    studyInfo = models.CharField(max_length=200, verbose_name='学习情况', default='暂无')
    studySuggestion = models.CharField(max_length=100, verbose_name='学习建议', default='暂无')
    reviewCorrectRates = models.IntegerField(verbose_name='复习正确率', default=0)
    reviewCorrectRatesRank = models.IntegerField(verbose_name='复习正确率排名', default=-1)
    daily_scores = models.CharField(max_length=20, verbose_name='每日成绩走向图', default='0,0,0,0,0')
    daily_units = models.CharField(max_length=20, verbose_name='每日单元数走向图', default='0,0,0,0,0')


    def __str__(self):
        return '<Profile: %s %s for %s>' % (self.nickname, self.user.username, self.dailyScores)

