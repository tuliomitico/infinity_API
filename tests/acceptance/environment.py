import shutil

from rest_framework.test import APIClient
from django.conf import settings

MEDIA_ROOT = settings.BASE_DIR / 'temp'

def django_ready(context):
  context.test.client = APIClient()

def after_all(context):
  shutil.rmtree(MEDIA_ROOT,ignore_errors=True)
