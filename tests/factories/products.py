from factory.django import DjangoModelFactory
import factory

from core.apps.products.models import Product


class ProductModelFactory(DjangoModelFactory):
    title = factory.Faker("first_name")
    description = factory.Faker("text")

    class Meta:
        model = Product