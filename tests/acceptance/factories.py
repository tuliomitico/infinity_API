import factory
from django.contrib.auth import get_user_model

from store.models import Store

class OwnerFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = get_user_model()
  id = 1
  cpf = '42246244005'
  username = factory.faker.Faker('first_name')
  password = factory.faker.Faker('password')
  telephone = factory.faker.Faker('phone_number')
  email = factory.faker.Faker('ascii_safe_email')

class StoreFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Store
  name = 'Loja 5'
  category = 'misc'
  description = factory.faker.Faker('text')
  lat = 123.0
  lng = -50.0
  slug = 'loja-5'
  logotype = factory.django.ImageField(color='blue')
  owner = factory.SubFactory(OwnerFactory)
