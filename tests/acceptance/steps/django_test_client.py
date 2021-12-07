from behave import when, then

@when(u'eu uso o cliente de teste Django para visitar "{url}"')
def use_django_client(context,url):
  context.response = context.test.client.get(url)

@then(u'deve retorna uma resposta de redirecionamento 302')
def it_should_be_successful(context):
  assert context.response.status_code == 302
