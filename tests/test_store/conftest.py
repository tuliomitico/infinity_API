import pytest

from django.contrib.auth import get_user_model

@pytest.fixture
def usuario():
  return get_user_model().objects.create(
    username='Rand',
    password='qwe',
    cpf='57952531620',
    email='rand@mail.com',
    telephone='7932100890'
  )
