from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic

# Create your views here.
def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request, 'first_app/index.html', context=date_dict)

def help(request):
	template_tags = {'base_page': 'First App'}
	return render(request, "first_app/help.html", context=template_tags)

def logos(request):
	template_tags = {}
	return render(request, "first_app/logos.html", context=template_tags)