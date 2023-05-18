from django.urls import path
from SignUp import views

app_name = 'signup'

urlpatterns = [
	path('', views.index, name='index')
]