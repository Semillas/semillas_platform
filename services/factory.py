# -*- coding: utf-8 -*-

import factory
import faker
import datetime

from django.conf import settings

from .models import Service
from .models import ServicePhoto
from semillas_backend.users.models import User

faker = faker.Factory.create()


class ServicePhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServicePhoto
    photo = factory.django.ImageField()


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=3))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=20))
    author = factory.Iterator(User.objects.all())
    date = factory.Sequence(lambda n: datetime.datetime.now() + datetime.timedelta(days=n))
    seeds_price = factory.Faker('pyint')

    photos = factory.RelatedFactory(ServicePhotoFactory, 'service')


