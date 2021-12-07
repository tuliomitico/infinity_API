import json

import factory
import pytest
from model_bakery import baker
from django.urls import reverse
from django_mock_queries.mocks import MockSet
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from store.models import Store

from tests.test_store.factories import OwnerFactory, StoreFactory
from store.views import StoreDetail, StoreList

pytestmark = [pytest.mark.urls('store.urls'),pytest.mark.unit]

class TestStoreViews(object):
  def test_list(self,mocker,rf):
    url = reverse('storecreate')
    request = rf.get(url)
    qs = MockSet(
      StoreFactory.build(),
      StoreFactory.build(),
      StoreFactory.build()
    )
    view = StoreList.as_view()
    mocker.patch.object(
      StoreList,'get_queryset',return_value=qs
    )
    response = view(request).render()
    assert response.status_code == 200
    assert len(json.loads(response.content)) == 3
  @pytest.mark.skip(reason='Ainda em descoberta')
  # @pytest.mark.django_db
  def test_retrieve(self,mocker,rf):
    store = StoreFactory.build()
    url = reverse('storedetail',kwargs={'pk':store.slug})
    request = rf.get(url)
    qs = MockSet(store)
    view = StoreDetail.as_view()
    mocker.patch.object(
      StoreDetail,'get_queryset',return_value=qs
    )
    response = view(request,pk=store.slug).render()
    print(request)
    expected_json = {
      'id': store.id,
      'name': store.name,
      'description': store.description,
      'category': store.category,
      'lat':store.lat,
      'lng':store.lng,
      'slug':store.slug,
      'owner':1,
      'logotype':'http://testserver/media/logo/default.png',
    }

    assert response.status_code == 200
    assert json.loads(response.content) == expected_json
  @pytest.mark.skip(reason="Ainda em descoberta")
  def test_create(self,mocker,rf):
    user = OwnerFactory.build()
    refresh = RefreshToken.for_user(user=user)
    valid_data_dict = factory.build(
      dict,
      FACTORY_CLASS = StoreFactory
    )
    url = reverse('storecreate')
    request = rf.post(
      url,
      content_type='multipart/form-data',
      data = valid_data_dict,
      HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
    )
    mocker.patch.object(
      Store,'save'
    )
    view = StoreList.as_view()
    response = view(request).render()

    assert response.status_code == status.HTTP_201_CREATED
