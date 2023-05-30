from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import Http404

from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import generics
from rest_framework import mixins
from rest_framework import serializers
import simplejson as json

from Employee.models import Company,Device,DeviceLog
from Employee.serializers import CompanySerializer,DeviceSerializer,DeviceLogSerializer
from django.template import loader

#################    GenericApiView based API     #################
#https://www.django-rest-framework.org/api-guide/generic-views/
#https://www.django-rest-framework.org/tutorial/3-class-based-views/
class GenericApiView_Company(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    lookup_field="id"

    #https://www.django-rest-framework.org/tutorial/3-class-based-views/
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=id):
        return self.destroy(request,id)
    
class GenericApiView_Device(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    lookup_field="id"

    #https://www.django-rest-framework.org/tutorial/3-class-based-views/
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=id):
        return self.destroy(request,id)
        
class GenericApiView_DeviceLog(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset=DeviceLog.objects.all()
    serializer_class=DeviceLogSerializer
    lookup_field="id"

    #https://www.django-rest-framework.org/tutorial/3-class-based-views/
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=id):
        return self.destroy(request,id)
    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")