from django.shortcuts import render

# dummy data

dummy_patients = [
	{
		"patient_id": 1,
		"first_name": "Malati",
		"last_name": "Chakraborty",
		"dob": "15-08-1947",
		"age": 75
	},
	{
		"patient_id": 2,
		"first_name": "Debasish",
		"last_name": "Chakraborty",
		"dob": "03-10-1961",
		"age": 61
	},
	{
		"patient_id": 3,
		"first_name": "Uttara",
		"last_name": "Chakraborty",
		"dob": "02-12-1968",
		"age": 54
	},
	{
		"patient_id": 4,
		"first_name": "Archisman",
		"last_name": "Chakraborty",
		"dob": "26-01-1999",
		"age": 24
	}
]

dummy_records = [
	{
		"type": "Blood Pressure",
		"value": "139/68 mm Hg",
		"day": 4,
		"month": 12,
		"year": 2022
	},
	{
		"type": "Blood Pressure",
		"value": "133/69 mm Hg",
		"day": 4,
		"month": 1,
		"year": 2023
	},
	{
		"type": "Blood Pressure",
		"value": "122/74 mm Hg",
		"day": 4,
		"month": 2,
		"year": 2023
	},
	{
		"type": "Blood Pressure",
		"value": "124/77 mm Hg",
		"day": 4,
		"month": 3,
		"year": 2023
	},
	{
		"type": "Blood Pressure",
		"value": "119/70 mm Hg",
		"day": 4,
		"month": 4,
		"year": 2023
	},
	{
		"type": "Blood Pressure",
		"value": "127/73 mm Hg",
		"day": 4,
		"month": 5,
		"year": 2023
	}
]

# Create your views here.

def index(request):
	inputs = {
		'login': [
			{'name': 'username', 'type': 'text', 'label': 'Username'}, 
			{'name': 'password', 'type': 'password', 'label': 'Password'}, 
		],
		'register': [
			{'name': 'fullname', 'type': 'text', 'label': 'Full Name'}, 
			{'name': 'username', 'type': 'text', 'label': 'Username'}, 
			{'name': 'email', 'type': 'email', 'label': 'Email ID'}, 
			{'name': 'password', 'type': 'password', 'label': 'Password'}, 
			{'name': 're-password', 'type': 'password', 'label': 'Confirm Password'}, 
		]
	}
	return render(request, 'main/index.html', context=inputs)

def dashboard(request):
	patient_details = [
		{
			"patient_id": patient["patient_id"],
			"first_name": patient["first_name"],
			"last_name": patient["last_name"]
		} for patient in dummy_patients
	]

	content = {
		'page_desc': "This is going to be a user dashboard page",
		'patient_list': patient_details			
	}

	return render(request, 'main/dashboard.html', context=content)

def patient_details_view(request, patient_id):

	patient_details = [patient for patient in dummy_patients if patient["patient_id"] == patient_id]
	records = [ f"{rec['day']}-{rec['month']}-{rec['year']}" for rec in dummy_records ]

	content = {
		'page_desc': "Patient Dashboard",
		'details': patient_details[0],
		'records': records
	}
	return render(request, 'main/patientDetails.html', context=content)

def patient_record_view(request, patient_id):	
	record_date = request.GET['recid']
	day, month, year = [int(part) for part in record_date.split("-")]
	record = [rec for rec in dummy_records 
		if rec['day'] == day and rec['month'] == month and rec['year'] == year
	]

	content = {
		'patient_id': patient_id,
		'record_date': record_date,
		'details': record[0]
	}
	return render(request, 'main/patientRecord.html', context=content)