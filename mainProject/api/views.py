from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.views import APIView
from .models import myApi
# Create your views here.

def main(request):
	 
    return HttpResponse("html")

from .serializers import myApiserializer

 
class mainhit(APIView):
	#permission_classes=[AllowAny,]
	def get(self, request, format=None):
		queryset = myApi.objects.all()
		serializer = myApiserializer(queryset, many=True)
		 
			 
		return Response(serializer.data) 
	 
    