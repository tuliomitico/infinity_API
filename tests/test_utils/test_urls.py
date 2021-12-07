class TestUtilsURLS(object):
  def test_swagger(self,api_client):
    client = api_client()
    response = client.get('/docs/')
    assert response.status_code == 200
