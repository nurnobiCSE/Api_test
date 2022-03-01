from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.views import APIView
from .models import myApi,skilModel,projectModel
# Create your views here.

def main(request):
	 
    return render(request,"home.html")

from .serializers import myApiserializer,skillApiserializer,projectApiserializer

 
class mainhit(APIView):
	#permission_classes=[AllowAny,]
	def get(self, request, format=None):
		queryset = myApi.objects.all()
		serializer = myApiserializer(queryset, many=True)
		 
			 
		return Response(serializer.data) 

class skilApi(APIView):
	def get(self,request, format=None):
		queryset = skilModel.objects.all()
		serializer = skillApiserializer(queryset, many=True)

		return Response(serializer.data)


class projectModelApi(APIView):
	def get(self,request, format=None):
		queryset = projectModel.objects.all()
		serializer = projectApiserializer(queryset, many=True)

		return Response(serializer.data)