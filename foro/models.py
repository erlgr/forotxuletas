from django.db import models


# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    bumped = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content
