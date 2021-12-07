import pytest
from store.models import Store
from django.contrib.auth import get_user_model

class TestStoreModels(object):

  @pytest.mark.django_db
  def test_create_model(self,usuario):
    lojinha = Store.objects.create(name='Loja 1',lat=123.0,lng=50,category='misc',owner=usuario)
    assert lojinha
  @pytest.mark.django_db
  def test_save_model(self,usuario):
    lojinha = Store(name='Loja 1',lat=123.0,lng=50,category='misc',owner=usuario)
    lojinha.save()
    assert type(lojinha.id) == int
    assert Store.objects.all().count() == 1
  @pytest.mark.django_db
  def test_delete_model(self,usuario):
    lojinha = Store(name='Loja 1',lat=123.0,lng=50,category='misc',description='Lorem Ipsum',slug='loja-1',owner=usuario)
    lojinha.save()
    lojinha.delete()
    assert Store.objects.all().count() == 0



