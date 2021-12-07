import pytest
from pytest_mock import MockerFixture
import factory

from tests.test_store.factories import OwnerFactory, StoreFactory, DeserializableStoreFactory
from store.serializers import StoreSerializer

class TestStoreSerializer():
  @pytest.mark.unit
  def test_serialize_model(self):
    store = StoreFactory.build()
    serializer = StoreSerializer(store)

    assert serializer.data

  @pytest.mark.django_db
  def test_serialized_data(self,mocker: MockerFixture):
    user = OwnerFactory()
    store = StoreFactory.build(owner=user)
    valid_serialized_data = {
      'name':store.name,
      'category': store.category,
      'description':store.description,
      'lat':store.lat,
      'lng':store.lng,
      'owner':store.owner.pk,
      'slug': store.slug,
      'logotype': store.logotype
    }

    serializer = StoreSerializer(data=valid_serialized_data)

    assert serializer.is_valid()
    assert serializer.errors == {}
