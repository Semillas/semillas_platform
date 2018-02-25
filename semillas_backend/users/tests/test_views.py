from test_plus.test import TestCase

from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.contrib.gis.geos import Point
from django.conf import settings
from django.urls import reverse

from semillas_backend.users.factory import UserFactory
from services.factory import categories

from semillas_backend.users.models import User


class BaseServiceTestCase(TestCase):

    def setUp(self):
        self.users = UserFactory.create_batch(size=2)
        self.factory = APIRequestFactory()
        self.client = APIClient()
        token = Token(user=self.users[0])
        token.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class TestUserDetailUpdate(BaseServiceTestCase):

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestUserDetailUpdate, self).setUp()

        # Create self.users, Services & Categories for test cases

    def test_user_update_basic(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word

        response = self.client.put(
            reverse('api_users:update', kwargs={'uuid':
                                                str(self.users[0].uuid)}),
            {"name": "New Name"}
        )

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIsInstance(
            response.data,
            dict
        )

        self.assertEqual(
            response.data["name"],
            "New Name"
        )

    def test_user_update_location(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word

        latitude = "40.4378698"
        longitude = "-3.8196228"

        self.client.default_format = 'json'
        response = self.client.put(
            reverse('api_users:update', kwargs={'uuid':
                                                str(self.users[0].uuid)}),
            {"location": {
                "latitude": latitude,
                "longitude": longitude
            }
            }
        )

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIsInstance(
            response.data,
            dict
        )

        self.assertEqual(
            response.data["location"]["longitude"],
            longitude
        )
        self.assertTrue(
            User.objects.get(uuid=response.data['uuid']).location_manually_set
        )

    def test_user_update_location_with_patch(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word

        latitude = "40.4378698"
        longitude = "-3.8196228"

        self.client.default_format = 'json'
        response = self.client.patch(
            reverse('api_users:update', kwargs={'uuid':
                                                str(self.users[0].uuid)}),
            {"location": {
                "latitude": latitude,
                "longitude": longitude
            }
            }
        )

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIsInstance(
            response.data,
            dict
        )

        self.assertEqual(
            response.data["location"]["longitude"],
            longitude
        )
        self.assertTrue(
            User.objects.get(uuid=response.data['uuid']).location_manually_set
        )
