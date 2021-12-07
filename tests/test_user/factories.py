import factory

from django.contrib.auth import get_user_model

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = get_user_model()
  cpf = '42246244005'
  username = factory.faker.Faker('first_name')
  password = factory.faker.Faker('password')
  telephone = factory.faker.Faker('phone_number')
  email = factory.faker.Faker('ascii_safe_email')

class DbUserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = get_user_model()
  username = 'tulio'
  cpf='20009610022'
  telephone = factory.faker.Faker('phone_number')
  email = factory.faker.Faker('ascii_safe_email')
  is_active = 1
  password ='qwe12345'
