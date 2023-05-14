from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import User
from AppTwo.forms import RegisterUserForm, SignUpForm

# Create your views here.
def index(request):
	return HttpResponse("<em>My Second App</em>")

def help(request):
	template_tags = {'base_page': 'Second App'}
	return render(request, "appTwo/help.html", context=template_tags)

def users(request):
	users = User.objects.all()
	users_dict = {'users': users}
	return render(request, "appTwo/users.html", context=users_dict)

def register_user_form_view(request):
	form = RegisterUserForm()

	if request.method == 'POST':
		form = RegisterUserForm(request.POST)

		if form.is_valid():
			print(f'Validated Data: ' \
			f'{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]} ' \
			f'with email as {form.cleaned_data["email"]}')

	return render(request, "appTwo/registerForm.html", {'form': form})

def signup_form_view(request):
	form = SignUpForm()

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			# first_name, last_name, email = form.cleaned_data.values()
			# user = User(first_name=first_name, last_name=last_name, email=email)
			# user.save()
			form.save(commit=True)
			return users(request)
		else:
			print('ERROR: FORM DATA INVALID')

	return render(request, "appTwo/signupForm.html", {'form': form})