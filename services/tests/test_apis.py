from test_plus.test import TestCase

from rest_framework.test import force_authenticate
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.contrib.gis.geos import Point
from django.conf import settings
from django.urls import reverse

from semillas_backend.users.factory import UserFactory
from services.factory import ServiceFactory
from services.factory import categories
from services.models import Category

from semillas_backend.users.models import User


class BaseServiceTestCase(TestCase):

    def setUp(self):
        self.users = UserFactory.create_batch(size=2)
        self.client = APIClient()
        token = Token(user=self.users[0])
        token.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class TestServiceDelete(BaseServiceTestCase):

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestServiceDelete, self).setUp()
        self.service = ServiceFactory(
            category=Category.objects.first(),
            author=self.users[0],
            title='1',
        )

    def test_owner_deletes_service(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word

        response = self.client.delete(
            reverse('api_service:delete', kwargs={'uuid':
                                                  str(self.service.uuid)}),
        )

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            204
        )

    def test_not_owner_deletes_service(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word

        self.service.author = self.users[1]
        self.service.save()

        response = self.client.delete(
            reverse('api_service:delete', kwargs={'uuid':
                                                  str(self.service.uuid)}),
        )

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            404
        )

    def test_staff_deletes_service(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word

        self.service.author = self.users[1]
        self.service.save()

        self.users[0].is_staff = True
        self.users[0].save()

        response = self.client.delete(
            reverse('api_service:delete', kwargs={'uuid':
                                                  str(self.service.uuid)}),
        )

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            204
        )
