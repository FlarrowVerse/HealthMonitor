from django.urls import path
from AppTwo import views

urlpatterns = [
	path('', views.index, name="index"),
	path('help', views.help, name="help"),
	path('users', views.users, name="users"),
	path('register', views.register_user_form_view, name="register"),
	path('signup', views.signup_form_view, name="signup"),
]

