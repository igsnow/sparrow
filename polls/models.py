import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 添加后使pycharm能够智能提示
    objects = models.Manager()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 这是个bug
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        # 只有当日期是过去式的时候才能返回True
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.choice_text
