from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	address	= models.CharField(blank=True, max_length=200)
	
	
def __str__(self):
  return self.user.username