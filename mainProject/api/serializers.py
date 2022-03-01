from rest_framework import serializers
 
from .models import myApi,skilModel,projectModel

class myApiserializer(serializers.ModelSerializer):
	class Meta:
		model = myApi
		#fields = '__all__'
		fields = ['id', 'name', 'email', 'mobile', 'address', 'gender']

class skillApiserializer(serializers.ModelSerializer):
	class Meta:
		model = skilModel
		fields = ['id', 'name', 'description', 'creator', 'progress_rate', 'ReleasDate']

class projectApiserializer(serializers.ModelSerializer):
	class Meta:
		model = projectModel
		fields = ['id', 'title', 'description', 'image', 'previewLink', 'sourceLink', 'ReleasDate']