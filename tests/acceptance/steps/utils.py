from behave import *

@given(u'a url da documentacao "{url}"')
def dado_docs(context,url):
  context.response = context.test.client.get(url)

@then(u'retorna sucesso "{code}"')
def retorna(context,code):
  assert context.response.status_code == int(code)
