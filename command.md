## Create Project
django-admin startproject drfecommerce

## Run django app
python manage.py runserver

## Import get_random_secret_key
from django.core.management.utils import get_random_secret_key

# Print value from get_random_secret_key
print(get_random_secret_key())