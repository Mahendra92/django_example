from django.db import models

# Create your models here.


class UserProfile(models.Model):
	user_name = models.CharField(max_length = 25)
	email_id = models.EmailField()
	password = models.CharField(max_length=20)