from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class todo_db(models.Model):

    title=models.CharField(max_length=100)
    memo=models.TextField(blank=True)
    created_date=models.DateTimeField(default=timezone.now())
    completed_date=models.DateTimeField(null=True,blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return( " %s %s "%(self.user,self.title))
