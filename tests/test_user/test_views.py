from django.http import response
import factory
import json
import pytest
from pytest_mock import MockerFixture
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model

from tests.test_user.factories import DbUserFactory, UserFactory
from user.views import CustomUserCreate, MyTokenObtainPairView

pytestmark = [pytest.mark.urls('user.urls'),pytest.mark.unit]


class TestUserViews(object):
  @pytest.mark.skip(reason="Ainda em descoberta")
  def test_create(self,mocker,rf):
    valid_data_dict = factory.build(
      dict,
      FACTORY_CLASS = UserFactory
    )
    url = reverse('create_user')
    request = rf.post(
      url,
      content_type='application/json',
      data=json.dumps(valid_data_dict)
    )
    mocker.patch.object(
      get_user_model(),
      'save'
    )
    view = CustomUserCreate.as_view()

    response = view(request).render()

    assert response.status_code == 201

  @pytest.mark.skip(reason='Ainda em descobertas')
  def test_login(self, mocker: MockerFixture, rf: RequestFactory):
    user = DbUserFactory.build()
    url = reverse('token_obtain_pair')
    request  = rf.post(
      url,
      content_type='application/json',
      data=json.dumps({'username':user.username,'password':user.password})
    )
    mocker.patch.object(
      MyTokenObtainPairView,
      'get_object',
      return_value = {
        'access':'123',
        'refresh':'123',
        'id':user.id,
        'username':user.username
      }
    )
    view = MyTokenObtainPairView.as_view()
    response = view(request).render()

    assert response.status_code == 200
