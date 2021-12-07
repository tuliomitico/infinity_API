import pytest

pytestmark = [pytest.mark.django_db]

class TestStoreURLS(object):
  def test_list(self,api_client):
    client = api_client()
    response = client.get('/store/')
    assert response.status_code == 200
