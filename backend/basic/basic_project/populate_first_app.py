import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social Network', 'Marketplace', 'News', 'Games']
def add_topic():	
	t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):
		topic = add_topic()

		# generated content
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		# webpage entry
		webpage = Webpage.objects.get_or_create(topic=topic, name=fake_name, url=fake_url)[0]

		# accessrecord entry
		access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
	print('populating database.....')
	populate(20)
	print('database population complete!')
		