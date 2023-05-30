from django.urls import path
from Employee.views import GenericApiView_Company,GenericApiView_Device,GenericApiView_DeviceLog
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path('company/',GenericApiView_Company.as_view(),name="company"),
    path('company/<int:id>/',GenericApiView_Company.as_view(),name="company"),

    path('device/',GenericApiView_Device.as_view(),name="device"),
    path('device/<int:id>/',GenericApiView_Device.as_view(),name="device"),

    path('devicelog/',GenericApiView_DeviceLog.as_view(),name="devicelog"),
    path('devicelog/<int:id>/',GenericApiView_DeviceLog.as_view(),name="devicelog"),
]