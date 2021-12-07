import json
from unittest import mock as mocker

from behave import *
import factory
from django.contrib.auth import get_user_model

from tests.acceptance.factories import OwnerFactory
from user.serializers import MyTokenObtainPairSerializer

@given(u'username="{user}" senha="{pwd}" cpf="{cpf}" telephone="{phone}" email="{email}"')
def quando_cadastrar(context,user,pwd,cpf,phone,email):
  context.response = context.test.client.post(
    '/user/create/',
    data={'username':user,'password':pwd,'cpf': cpf,'telephone':phone,'email': email},
    format='json'
  )

@when(u'logar com o usuario "{user}" e senha "{pwd}"')
def quando_logar(context,user,pwd):
  context.response = context.test.client.post('/login/',data={'username':user,'password':pwd},format="json")

@then(u'sucesso')
def logado(context):
  assert context.response.status_code == 200
  assert 'access' in json.loads(context.response.content).keys()
