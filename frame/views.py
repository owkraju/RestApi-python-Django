from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer
from rest_framework import status
class DataList(viewsets.ModelViewSet):
	    queryset = Data.objects.all()
    	    serializer_class = DataSerializer

"""
def get(self,request):
		emp=Data.objects.all()
		serializer=DataSerializer(emp,many=True)
		return Response(serializer.data)
	def post(self,request):
		emp=DataSerializer(data=request.data)
		if emp.is_valid():
			emp.save()
			return Response(emp.data)
		return Response(emp.data)"""
"""class DataDetails(APIView):
	def get_object(self, id):
		try:
			return Data.objects.get(id=id)
		except Data.DoesNotExist:
			return HttpResponse("Data not found")
	def get(self,request,id):
		try:
			d=self.get_object(id)
			serializer=DataSerializer(d)
			return Response(serializer.data)
		except:
			return Response(status=status.HTTP_204_NO_CONTENT)
	def put(self, request,id):
		try:
			d=self.get_object(id)
			emp=DataSerializer(d,data=request.data)
			if emp.is_valid():
				emp.save()
				return Response(emp.data)
			return Response(emp.data)
		except:
			return Response(status=status.HTTP_204_NO_CONTENT)
	def delete(self,request,id):
		try:
			d=self.get_object(id)
			d.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		except:
			return Response(status=status.HTTP_204_NO_CONTENT)
"""
