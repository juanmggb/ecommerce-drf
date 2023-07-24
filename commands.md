# Packages

asgiref==3.7.2
attrs==23.1.0
black==23.7.0
click==8.1.6
colorama==0.4.6
coverage==7.2.7
Django==4.2.3
django-js-asset==2.1.0
django-mptt==0.14.0
djangorestframework==3.14.0
drf-spectacular==0.26.3
factory-boy==3.3.0
Faker==19.2.0
inflection==0.5.1
iniconfig==2.0.0
jsonschema==4.18.4
jsonschema-specifications==2023.7.1
mypy-extensions==1.0.0
packaging==23.1
pathspec==0.11.1
Pillow==10.0.0
platformdirs==3.9.1
pluggy==1.2.0
Pygments==2.15.1
pytest==7.4.0
pytest-cov==4.1.0
pytest-cover==3.0.0
pytest-coverage==0.0
pytest-django==4.5.2
pytest-factoryboy==2.5.1
python-dateutil==2.8.2
python-dotenv==1.0.0
pytz==2023.3
PyYAML==6.0.1
referencing==0.30.0
rpds-py==0.9.2
six==1.16.0
sqlparse==0.4.4
typing_extensions==4.7.1
tzdata==2023.3
uritemplate==4.1.1

# Commands

django-admin startproject backend .
python manage.py runserver
from django.core.management.utils import get_secret_key
print(get_secret_key())
pip install --upgrade pip

# Pytest

pytest -h # prints options _and_ config file settings
python manage.py spectacular --file schema.yml

# Coverage

coverage run -m pytest
coverage html

# Pytest-coverage

pytest --cov
