from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.TextField()
    posted_on = models.DateTimeField()
    posted_by = models.TextField()