import json
from io import BytesIO
import shutil

import pytest
import factory
from model_bakery import baker
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.files import File
from django.test import override_settings
from PIL import Image

from store.models import Store

pytestmark = pytest.mark.django_db
MEDIA_ROOT: str = settings.BASE_DIR / 'temp'

class TestStoreEndpoints(object):

  endpoint: str = '/store/'
  logo: str = 'http://testserver/media/logo/default.png'

  def teardown_class(self) -> None:
    """Remove o diretorio com as imagens geradas"""
    shutil.rmtree(MEDIA_ROOT,ignore_errors=True)

  def test_list(self,api_client):
    baker.make(Store,_quantity=3)

    response = api_client().get(
      self.endpoint
    )

    assert response.status_code == 200
    assert len(json.loads(response.content)) == 3

  @override_settings(MEDIA_ROOT=MEDIA_ROOT)
  def test_create(self,api_client):
    user = baker.make(get_user_model(),cpf='42246244005')
    refresh = RefreshToken.for_user(user=user)
    store = baker.prepare(Store,category="misc")
    file_obj = BytesIO()
    image = Image.new("RGBA", size=(50,50), color=(256,0,0))
    image.save(file_obj, 'png')
    file_obj.seek(0)
    file = File(file_obj, name='logo.png')
    expected_json = {
      'name': store.name,
      'description': store.description,
      'category': store.category,
      'lat': store.lat,
      'lng': store.lng,
      'slug': store.slug,
      'logotype': file,
      'owner': user.pk
    }
    client = api_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    response = client.post(
      self.endpoint,
      data = expected_json,
      format = 'multipart',
    )
    print(response.content)
    expected_json['id'] = 1
    expected_json['logotype'] = f'http://testserver/media/logo/logo.png'
    assert response.status_code == 201
    assert json.loads(response.content) == expected_json

  def test_retrieve(self,api_client):
    store = baker.make(Store,name='Loja 1',slug='loja-1')
    expected_json = {
      'name': store.name,
      'description': store.description,
      'category': store.category,
      'lat': store.lat,
      'lng': store.lng,
      'slug': store.slug,
      'logotype': self.logo,
      'owner': 1
    }
    url = f'{self.endpoint}loja-1/'

    response = api_client().get(url)
    expected_json['id'] = 1
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json

  def test_update(self,rf,api_client):
    user = baker.make(get_user_model(),cpf='42246244005')
    refresh = RefreshToken.for_user(user=user)
    old_store = baker.make(Store,owner=user)
    new_store = baker.prepare(Store)
    store_dict = {
      'name': new_store.name,
      'description': new_store.description,
      'category': new_store.category,
      'lat': new_store.lat,
      'lng': new_store.lng,
      'owner': user.id,
      'slug': new_store.slug
    }

    url = f'{self.endpoint}{old_store.id}/'
    client = api_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    response = client.put(
      url,
      store_dict,
      format='json'
    )
    store_dict['id'] = 1
    store_dict['logotype'] = self.logo
    assert response.status_code == 200
    assert json.loads(response.content) == store_dict

  @pytest.mark.parametrize('field',[
    ('name'),
    ('slug'),
    ('category'),
    ('description'),
    ('lat'),
    ('lng'),
    ('owner')
  ])
  def test_partial_update(self, mocker, rf, field, api_client):
      user = baker.make(get_user_model(),cpf='42246244005')
      refresh = RefreshToken.for_user(user=user)
      store = baker.make(Store,owner=user)
      store_dict = {
          'name': store.name,
          'slug': store.slug,
          'category': store.category,
          'description': store.description,
          'lat': store.lat,
          'lng': store.lng,
          'owner': user.id,
      }
      valid_field = store_dict[field]
      url = f'{self.endpoint}{store.id}/'
      client = api_client()
      client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
      response = client.patch(
          url,
          {field: valid_field},
          format='json'
      )

      assert response.status_code == 200
      assert json.loads(response.content)[field] == valid_field

  def test_delete(self,mocker,api_client):
    user = baker.make(get_user_model(),cpf='42246244005')
    refresh = RefreshToken.for_user(user=user)
    store = baker.make(Store,owner=user)

    url= f"{self.endpoint}delete/{store.id}/"
    client = api_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    response = client.delete(url)

    assert response.status_code == 204
    assert Store.objects.all().count() == 0
