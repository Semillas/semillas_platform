# -*- coding: utf-8 -*-
import factory
from django.contrib.gis.geos import Point
from wallet.factory import WalletFactory
from .models import User

class UserFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = User  # Equivalent to ``model = myapp.models.User``
		#django_get_or_create = ('username',)

	name = factory.Faker('name')
	email = factory.Faker('email')
	username = factory.Faker('name')
	location = Point(-3.7035285, 40.4169473) # Puerta del Sol, Madrid
	picture = factory.django.ImageField()
	wallet = factory.RelatedFactory(WalletFactory, 'owner')
