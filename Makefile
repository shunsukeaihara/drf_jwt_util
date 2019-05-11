i18n:
	cd drf_jwt_util;\
	django-admin makemessages -l en;\
	django-admin makemessages -l ja;\
	django-admin.py compilemessages

upload:
	python setup.py sdist upload

all: i18n upload
