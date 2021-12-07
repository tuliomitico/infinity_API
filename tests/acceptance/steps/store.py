import json
from behave import *

from django.test import override_settings

from factories import StoreFactory
from tests.acceptance.environment import MEDIA_ROOT

@when(u'acessar "{url}"')
def lojas(context,url):
  with override_settings(MEDIA_ROOT=MEDIA_ROOT):
    store = StoreFactory()
  context.response = context.test.client.get(url)


@then(u'retornar sucesso')
def listado(context):
  assert context.response.status_code == 200
  assert len(context.response.content)

@when(u'acessar a busca "{url}"')
def procurar(context,url):
  with override_settings(MEDIA_ROOT=MEDIA_ROOT):
    store = StoreFactory()
  context.response = context.test.client.get(url)

@then(u'retornar outro sucesso')
def achado(context):
  assert context.response.status_code == 200
  assert len(json.loads(context.response.content)) == 1
