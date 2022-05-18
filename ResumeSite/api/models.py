from django.db import models

class Room(models.Model):
	code=models.CharField(max_length=8,default="",unique=True)
	host=models.CharField(max_length=50,unique=True)
	