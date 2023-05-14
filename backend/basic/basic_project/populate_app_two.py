import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_project.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
	for entry in range(N):
		
		# generated content
		fake_name = fakegen.name()
		fake_name_parts = fake_name.split(' ')
		fake_first_name = fake_name_parts[0]
		fake_last_name = fake_name_parts[-1]
		if len(fake_name_parts) > 2:
			fake_first_name += ' ' + ' '.join(fake_name_parts[1:-1])
		
		fake_email = fakegen.email()

		# user entry
		user = User.objects.get_or_create(
			first_name=fake_first_name, 
			last_name=fake_last_name,
			email=fake_email
		)[0]

if __name__ == '__main__':
	print('populating database.....')
	populate(100)
	print('database population complete!')
		