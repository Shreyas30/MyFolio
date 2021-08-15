from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your models here.
class SubscribedUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    subsType = models.IntegerField()                    # Subscription Type : 1-Personal  2-Professional 3-Premium  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    posts = models.CharField(max_length=1000,default='')
    followers = models.CharField(max_length=1000,default='')
    followings = models.CharField(max_length=1000,default='')
    jobTitle = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000,default='')
    profilePic = models.CharField(max_length=100,default='')
    resume = models.CharField(max_length=100,default='')
    portfolio = models.CharField(max_length=100,default='')    

    def __str__(self):
        return self.user_name

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField()
    content = models.CharField(max_length=1000)
    image = models.CharField(max_length=100,default='')
    time = models.DateTimeField()
