from rest_framework import serializers
 
from api.models import myApi

class myApiserializer(serializers.ModelSerializer):
	class Meta:
		model = myApi
		#fields = '__all__'
		fields = ['id', 'name', 'email', 'mobile', 'address', 'gender']

