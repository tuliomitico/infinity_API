import json
import factory

import pytest
from pytest_mock import MockerFixture
from model_bakery import baker
from django.contrib.auth import get_user_model
from django.test.client import RequestFactory
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.test_user.factories import DbUserFactory

pytestmark = pytest.mark.django_db

class TestUserEndPoints(object):

  endpoint = '/user/'

  def test_create(self,api_client: APIClient):
    user = baker.prepare(get_user_model(),cpf="42246244005")

    expected_json = {
      "username": user.username,
      "email": user.email,
      "cpf":  user.cpf,
      "password": user.password,
      "telephone": user.telephone,
    }
    response = api_client().post(
      self.endpoint + "create/",
      data = expected_json,
      format='json'
    )

    assert response.status_code == 201
    assert (response.content).decode('utf-8') == ''

  def test_not_create(self,api_client: APIClient):
    user = baker.prepare(get_user_model(),cpf='12345678910')
    response = api_client().post(
      self.endpoint + "create/",
      data = {
        'username': user.username,
        'password': user.password,
        'cpf': user.cpf,
        'telephone': user.telephone,
        'email': user.email,
      },
      format = 'json'
    )

    assert response.status_code == 400
    assert 'cpf' in json.loads(response.content).keys()

  def test_delete(self,api_client: APIClient):
    user = baker.make(get_user_model(),cpf='57952531620')
    url = f"{self.endpoint}delete/"
    refresh = RefreshToken.for_user(user)
    client = api_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    response = client.delete(url)

    assert response.status_code == 204
    assert get_user_model().objects.all().count() == 0

  @pytest.mark.parametrize('field',[('first_name'),('email'),('telephone')])
  def test_partial_update(self, mocker: MockerFixture, rf: RequestFactory, field, api_client: APIClient):
    user = baker.make(get_user_model(),cpf='20009610022',id=1)
    url = f"{self.endpoint}delete/"
    refresh = RefreshToken.for_user(user)
    user_dict = {
      'first_name': 'Jorginho',
      'email': user.email,
      'telephone': user.telephone,
    }
    valid_field = user_dict[field]

    client = api_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    response = client.patch(
      url,
      {field: valid_field},
      format='json'
    )

    assert response.status_code == 200
    assert json.loads(response.content)[field] == valid_field

  def test_no_partial_update(self, mocker: MockerFixture, rf: RequestFactory, api_client):
    user = baker.make(get_user_model(),cpf='20009610022',id=1)
    url = f"{self.endpoint}delete/"
    refresh = RefreshToken.for_user(user)
    user_dict = {
      'is_active': 'aab',
    }

    client = api_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    response = client.patch(
      url,
      data = user_dict,
      format='json'
    )

    assert response.status_code == 400

  def test_login(self, api_client: APIClient):
    user_dict = factory.build(
      dict,
      FACTORY_CLASS = DbUserFactory
    )
    user = get_user_model().objects.create_user(**user_dict)
    url = '/login/'
    client = api_client()
    response = client.post(
      url,
      data = {
        'username': user_dict['username'],
        'password': user_dict['password']
      },
      format='json'
    )

    assert response.status_code == 200
    assert  all(x in ['access','refresh','username','id'] for x in json.loads(response.content).keys())

