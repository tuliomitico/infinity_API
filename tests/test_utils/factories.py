import factory

class MyModelFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = MyModel
  field1 = factory.faker.Faker('relevant_generator')
