# -*- coding: utf-8 -*-

import factory
import faker
import datetime

from django.conf import settings

from .models import Service, Category, ServicePhoto
from semillas_backend.users.models import User

faker = faker.Factory.create()
categories=[
	"Atención a las personas",
	"Tareas domésticas",
	"Cuidado del cuerpo y la salud",
	"Construcción, reparaciones, jardinería",
	"Transporte y distribución",
	"Ocio y deportes",
	"Cultura y artes",
	"Música y baile",
	"Educación y formación",
	"Medio ambiente",
	"Animación, artesanía, hobbies",
	"Asesoramiento y orientación",
	"Idiomas",
	"Informática",
	"Gestión y administración"
]


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
    category = factory.Iterator(Category.objects.all())
    date = factory.Sequence(lambda n: datetime.datetime.now() + datetime.timedelta(days=n))
    seeds_price = factory.Faker('pyint')
    photo1 = factory.RelatedFactory(ServicePhotoFactory, 'service')
    photo2 = factory.RelatedFactory(ServicePhotoFactory, 'service')
    photo3 = factory.RelatedFactory(ServicePhotoFactory, 'service')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

#    order=Category.objects.count()
#    print(str(order))
#    name = categories[order]
#    if not name:
#        name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=3))
