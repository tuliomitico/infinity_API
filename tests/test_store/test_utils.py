from typing import Type
import pytest

from store.models import upload_to
from tests.test_store.factories import StoreFactory

@pytest.mark.unit
def test_formatador_de_path():
  assert upload_to(StoreFactory.build(),'default.png') == 'logo/default.png'
