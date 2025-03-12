# Packages

Django==5.1.6
pytest==8.3.5
python-dotenv==1.0.1
djangorestframework==3.15.2
pytest-django==4.10.0
django-mptt==0.16.0
drf-spectacular

# Commands

pip install requirement.txt

django-admin startproject drfecommerce

python manage.py runserver

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

pip install --upgrade pip

python manage.py spectacular --file schema.yml