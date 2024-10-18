import factory
from consumer.models.consumer import Consumer


class ConsumerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Consumer
