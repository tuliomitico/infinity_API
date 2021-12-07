import factory
import pytest
from pytest_mock import MockerFixture

from django.contrib.auth import get_user_model
from tests.test_user.factories import UserFactory, DbUserFactory
from user.serializers import UserSerializer, MyTokenObtainPairSerializer, RegisterUserSerializer

class TestUserSerializer(object):

  @pytest.mark.unit
  def test_user_serialize_model(self):
    user = UserFactory.build()
    serializer = UserSerializer(user)

    assert serializer.data

  @pytest.mark.django_db
  def test_user_serialized_data(self,mocker):
    user = DbUserFactory.build()
    valid_serialized_data = {
      'username': user.username,
      'password': user.password,
      'cpf': user.cpf,
      'telephone': user.telephone,
      'email': user.email,
    }

    serializer = UserSerializer(data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}

  @pytest.mark.unit
  def test_register_serialize_model(self):
    user = UserFactory.build()
    serializer = RegisterUserSerializer(user)

    assert serializer.data

  @pytest.mark.django_db
  def test_register_serialized_data(self,mocker):
    valid_serialized_data = factory.build(
      dict,
      FACTORY_CLASS = UserFactory
    )

    serializer = RegisterUserSerializer(data=valid_serialized_data)

    assert serializer.is_valid()
    assert serializer.errors == {}

  @pytest.mark.unit
  def test_token_serialize_model(self):
    user = UserFactory.build()
    serializer = MyTokenObtainPairSerializer(user)

    assert serializer.data
  @pytest.mark.skip(reason='Não está funcionando nesta modalidade. Vide:https://github.com/jazzband/djangorestframework-simplejwt/blob/master/tests/test_serializers.py')
  @pytest.mark.django_db
  def test_token_serialized_data(self,mocker: MockerFixture):
    user_dict = factory.build(
      dict,
      FACTORY_CLASS = DbUserFactory
    )
    user = get_user_model().objects.create_user(**user_dict)
    valid_serialized_data = {
      MyTokenObtainPairSerializer.username_field: user.username,
      'password': user.password
    }
    print(user_dict)
    print(valid_serialized_data)
    serializer = MyTokenObtainPairSerializer(context=mocker.MagicMock(),data=valid_serialized_data)

    assert serializer.is_valid(raise_exception=True)
    assert serializer.errors == {}
