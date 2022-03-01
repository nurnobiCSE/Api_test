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
class skilModel(models.Model):
    name =models.CharField(max_length=25,blank=False)
    description =models.CharField(max_length=500,blank=False)
    creator =models.CharField(max_length=25,blank=False)
    progress_rate =models.CharField(max_length=25,blank=False)
    ReleasDate =models.CharField(max_length=25,blank=False)

    def __str__(self):
        return self.name

class projectModel(models.Model):
    title = models.CharField(max_length=250,blank=False)
    description =models.CharField(max_length=500,blank=False)
    image = models.ImageField(upload_to='projectModelImg/')
    previewLink = models.CharField(max_length=500,blank=False)
    sourceLink = models.CharField(max_length=500,blank=False)
    ReleasDate = models.CharField(max_length=25,blank=False)