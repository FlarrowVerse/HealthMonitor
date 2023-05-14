# Health Monitoring App

I created this application because my parents asked me to keep a track of all relevant medical stats for my family members.

As usual my programmer brain starts ticking and I come up with this app.

## Technology used

Framework: **Django**

Database: **Sqlite3**

Languages Used: 

1. **Python**
2. **HTML**
3. **CSS**

## Installation Steps

1. First and foremost download the important folders only.

	a) What's important you ask? Well when I started learning Django I did some refresher projects on my web dev fundamentals.
	
	b) So in both backend and frontend folders there are some basic projects. Download them if you want to play with them. Not important for this app to work.

	c) Design folder is important if you want to know what my thinking was while designing the db. You can suggest changes to them for a better design as well.

	d) The project is fully contained under:

	_/backend/HealthMonitor_

2. I would suggest you to create a virtual environment with python to run the django in. Lots of tutorials online on how to do that. I will tell you what I did:

	a)  `pip install virtualenv`

	Do the above step to install virtualenv

	b) `virtualenv djangoEnv`

	c) On Linux
	
	`source djangoEnv/bin/activate`

3. Next I installed django directly using 

	`pip install Django`

	or

	`pip install django`

4. If you face some problems and want to use the exact versions of django and other libs run the following command:

	```pip install -r requirements.txt```

5. To run the application on localhost:

```
cd HealthMonitor
python manage.py runserver
```

6. Open your favorite browser and visit 
[HealthMonitorApp](http://localhost:8000)

## Promise

I will try to deploy this app once its done or release a dockerzed solution