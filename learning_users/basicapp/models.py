from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    #course does not account for required on delete when inheriting from other models

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional classes
    Portfolio_site = models.URLField(blank=True)

    Profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
