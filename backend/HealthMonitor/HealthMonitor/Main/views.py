from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('''
	<h1>This is the Main application</h1>
	<a href="http://localhost:8000/">Go to SignUp App</a>
	''')

def dashboard(request):
	content = {'page_desc': "This is going to be a user dashboard page"}
	return render(request, 'main/dashboard.html', context=content)

def patient_details_view(request, patient_id):
	content = {
		'page_desc': f"This is going to be a patient dashboard page for patient with id {patient_id}"
	}
	return render(request, 'main/patientDetails.html', context=content)

def patient_record_view(request, patient_id):
	record_date = request.GET['recid']
	content = {
		'patient_id': patient_id,
		'record_date': record_date
	}
	return render(request, 'main/patientRecord.html', context=content)