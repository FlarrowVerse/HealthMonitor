from django.urls import path
from Main import views

urlpatterns = [
	path('', views.index, name='index'),
	path('dashboard', views.dashboard, name='user-dash'),
	path('patient/<int:patient_id>', views.patient_details_view, name='patient-dash'),
	path('patient/<int:patient_id>/records', views.patient_record_view, name='record'),
]