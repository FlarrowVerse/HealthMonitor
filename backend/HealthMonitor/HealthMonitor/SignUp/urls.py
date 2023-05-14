from django.urls import path
from SignUp import views

urlpatterns = [
	path('', views.index, name='index')
]