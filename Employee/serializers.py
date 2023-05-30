from Employee.models import Company,Device,DeviceLog
from rest_framework import serializers
#from myapp.serializers import ArticleSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
