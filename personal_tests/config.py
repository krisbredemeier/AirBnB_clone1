import os

ENV = os.environ.get('AIRBNB_ENV', '')
# Hacky way of switching to test env
test = False
if test:
	ENV = 'test'

# DEV
if ENV == 'development':
	DEBUG = True
	HOST = '127.0.0.1'
	PORT = 3333
	DATABASE = {
		'host': '158.69.84.192',# IP address for web-01
		'user':'airbnb_user_dev',
		'database': 'airbnb_dev',
		'port': '3306',
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV', '')
	}
# PROD
elif ENV == 'production':
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
# TEST
elif ENV == 'test':
	DEBUG = False
	HOST = '127.0.0.1'
	PORT = 5555
	DATABASE = {
		'host': '158.69.84.192',# IP address for web-01,
		'user':'airbnb_user_test',
		'database': 'airbnb_test',
		'port': '3306',
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_TEST', '')
	}

# ERRORS
else:
	raise Exception("Could not evaluate the AIRBNB_ENV")
