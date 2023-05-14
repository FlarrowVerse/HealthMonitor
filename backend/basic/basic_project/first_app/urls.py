from django.urls import path
from first_app import views

urlpatterns = [
	path('', views.index, name="index"),
    path('logos', views.logos, name="logos"),
	path('help', views.help, name="help"),
]

'''
path('<url path here>', views.<function name of view here>, name="<view name here>")
'''