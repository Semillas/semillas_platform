from django.test import RequestFactory

from test_plus.test import TestCase

from ..views import (
    FeedServiceList
)

import ipdb;

from django.contrib.gis.geos import Point

from semillas_backend.users.factory import UserFactory
from services.factory import ServiceFactory, CategoryFactory
from services.factory import categories

from services.models import Service, Category


class BaseServiceTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

class TestFeedServiceList(BaseServiceTestCase):

    def tearDown(self):
        Category.objects.all().delete()

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestFeedServiceList, self).setUp()

        # Instantiate the view directly. Never do this outside a test!
        self.view = FeedServiceList()

        # Create self.users, Services & Categories for test cases
        if not hasattr(self, 'users'):

            self.users = UserFactory.create_batch(size=5)
            for i in range(len(categories)):
                CategoryFactory(name=categories[i],order=i)
            self.services = ServiceFactory.create_batch(size=5)
            
            # Create some locations
            location_madrid = Point(-3.8196228, 40.4378698) # Madrid 0
            location_paris = Point(2.3488, 48.8534) # Paris 1
            location_london = Point(-0.3817834, 51.528308) # London 2
            location_berlin = Point(13.4105, 52.5244) # Berlin 3
            location_rome = Point(12.395912, 41.909986) # Rome 4

            # Update locations on each of the self.users
            self.users[0].location = location_madrid
            self.users[0].save()
            self.users[1].location = location_paris
            self.users[1].save()
            self.users[2].location = location_london
            self.users[2].save()
            self.users[3].location = location_berlin
            self.users[3].save()
            self.users[4].location = location_rome
            self.users[4].save()

            # Assign each service to 1 of the self.users
            self.services[0].author = self.users[0]
            self.services[0].title = "1"
            self.services[0].description = "testing"
            self.services[0].save()
            self.services[1].author = self.users[1]
            self.services[1].title = "2"
            self.services[1].description = "testing"
            self.services[1].save()
            self.services[2].author = self.users[2]
            self.services[2].title = "3"
            self.services[2].description = "testing"
            self.services[2].save()
            self.services[3].author = self.users[3]
            self.services[3].title = "4"
            self.services[3].description = "testing"
            self.services[3].save()
            self.services[4].author = self.users[4]
            self.services[4].title = "5"
            self.services[4].description = "testing"
            self.services[4].save()
        
        

    def test_response_check_distances(self):

        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?search=testing')
        # Attach the user to the request
        request.user = self.users[3]

        self.view = FeedServiceList.as_view()
        response = self.view(request)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIsInstance(
            response.data, 
            list
        )

        self.assertEqual(
            [item["title"] for item in response.data],
            ["4", "2", "3", "5", "1"]
        )

        # def test_category_filtering(self):

        Service.objects.all().update(category=Category.objects.first())
        serv = Service.objects.first()
        serv.category = Category.objects.last()
        cat = Category.objects.last()
        serv.save()
        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?category='+str(cat.id))
        # Attach the user to the request
        request.user = self.users[3]

        self.view = FeedServiceList.as_view()
        response = self.view(request)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            len(response.data),
            1
        )

        self.assertEqual(
            response.status_code,
            200
        )

        # def test_wrong_category(self):

        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?category=2000000')
        # Attach the user to the request
        request.user = self.users[3]

        self.view = FeedServiceList.as_view()
        response = self.view(request)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            len(response.data),
            0
        )


