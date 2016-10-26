from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choise(models.Model):
    def __str__(self):
        return self.choise_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

