import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField('question', max_length=200)
    pub_date = models.DateTimeField('Publish date')
    def was_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text
     

class Choice(models.Model):
    asking = models.ForeignKey(Question, on_delete=models.CASCADE,)
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return f'{self.asking} Choice'
    
    