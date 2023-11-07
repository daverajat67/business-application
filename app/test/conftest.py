import os
import django
from bussinessapp import settings  # Replace with your project name

os.environ['DJANGO_SETTINGS_MODULE'] = 'bussinessapp.settings'
django.setup()