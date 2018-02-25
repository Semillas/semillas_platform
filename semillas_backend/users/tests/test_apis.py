from test_plus.test import TestCase


from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from django.contrib.gis.geos import Point
from django.conf import settings
from django.urls import reverse


from ..views import UserDetailUpdate
from ..factory import UserFactory
from semillas_backend.users.models import User


class BaseServiceTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

class TestUserDetailUpdate(BaseServiceTestCase):

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestUserDetailUpdate, self).setUp()

        # Instantiate the view directly. Never do this outside a test!
        self.view = UserDetailUpdate()

        # Create self.users, Services & Categories for test cases
        self.user = UserFactory(password='secret')

    def skip_test_update_user(self):
        """ This tests ask the feed without lat and lon and expects
        the lat and lon are retrieved from user model saved in db
        """

        # Generate a request search for "testing" key word
        request = self.factory.patch(reverse('api_users:update', kwargs={'uuid':self.user.uuid}), {'telephone': '+34679923601'})
        # Attach the user to the request
        force_authenticate(request, user=self.user)

        self.view = UserDetailUpdate.as_view()
        response = self.view(request)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )
