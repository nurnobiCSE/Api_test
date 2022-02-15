from django.db import models

# Create your models here.
class myApi(models.Model):
	name = models.CharField(max_length=15,blank=False)
	email = models.CharField(max_length=15,blank=False)
	mobile = models.CharField(max_length=15,blank=False)
	address = models.CharField(max_length=25,blank=False)
	gender = models.CharField(max_length=15,blank=False)

	# def __str__(self):
	# 	return self.name