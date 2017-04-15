import os

ENV = os.environ.get('AIRBNB_ENV', '')

# PROD
if ENV == 'production':
	DEBUG = False
	HOST = '0.0.0.0'
	PORT = 3000
	DATABASE = {
		'host': '158.69.84.192',# IP address for web-01,
		'user':'airbnb_user_prod',
		'database': 'airbnb_prod',
		'port': '3306',
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD', '')
	}
# ERRORS
else:
	DEBUG = True
	HOST = '0.0.0.0'
	PORT = 3333
	DATABASE = {
		'host': '0.0.0.0',# IP address for web-01
		'user':'airbnb_user_dev',
		'database': 'airbnb_dev',
		'port': '3306',
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV', '')
	}
