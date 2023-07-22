# Packages

asgiref==3.7.2
black==23.7.0
click==8.1.6
colorama==0.4.6
Django==4.2.3
djangorestframework==3.14.0
iniconfig==2.0.0
mypy-extensions==1.0.0
packaging==23.1
pathspec==0.11.1
platformdirs==3.9.1
pluggy==1.2.0
pytest==7.4.0
pytest-django==4.5.2
python-dotenv==1.0.0
pytz==2023.3
sqlparse==0.4.4
tzdata==2023.3

# Commands

django-admin startproject backend .
python manage.py runserver
from django.core.management.utils import get_secret_key
print(get_secret_key())
pip install --upgrade pip

# Pytest

pytest -h # prints options _and_ config file settings
