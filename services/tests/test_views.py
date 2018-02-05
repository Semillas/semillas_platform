from test_plus.test import TestCase

from ..views import FeedServiceList
from ..views import ServiceDetail
from ..views import UserServiceList
from ..serializers import ServiceSerializer

from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from django.contrib.gis.geos import Point
from django.conf import settings
from django.urls import reverse

from semillas_backend.users.factory import UserFactory
from services.factory import ServiceFactory, CategoryFactory
from services.factory import categories

from services.models import Service, Category
from semillas_backend.users.models import User


class BaseServiceTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()


class TestFeedServiceList(BaseServiceTestCase):

    # def tearDown(self):
    #    Category.objects.all().delete()

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestFeedServiceList, self).setUp()

        # Instantiate the view directly. Never do this outside a test!
        self.view = FeedServiceList.as_view()

        # Create self.users, Services & Categories for test cases
        self.users = UserFactory.create_batch(size=5)
        self.services = ServiceFactory.create_batch(
            size=5,
            category=Category.objects.first()
        )

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

    def test_response_check_distances_saved_in_user(self):
        """ This tests ask the feed without lat and lon and expects
        the lat and lon are retrieved from user model saved in db
        """

        # Create some locations
        location_madrid = Point(-3.8196228, 40.4378698)  # Madrid 0
        location_paris = Point(2.3488, 48.8534)  # Paris 1
        location_london = Point(-0.3817834, 51.528308)  # London 2
        location_berlin = Point(13.4105, 52.5244)  # Berlin 3
        location_rome = Point(12.395912, 41.909986)  # Rome 4

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

        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?search=')
        # Attach the user to the request
        force_authenticate(request, user=self.users[3])
        #request.user = self.users[3]

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

    def test_response_check_distances_anonymous_user_sending_params(self):
        """ This tests ask the feed without lat and lon and expects
        the lat and lon are retrieved from user model saved in db
        """

        # Create some locations
        location_madrid = Point(-3.8196228, 40.4378698)  # Madrid 0
        location_paris = Point(2.3488, 48.8534)  # Paris 1
        location_london = Point(-0.3817834, 51.528308)  # London 2
        location_berlin = Point(13.4105, 52.5244)  # Berlin 3
        location_rome = Point(12.395912, 41.909986)  # Rome 4

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

        # Generate a request search for "testing" key word
        request = self.factory.get(
            '/api/v1/service/feed?lat=%s&lon=%s' % (
                location_berlin.coords[1],
                location_berlin.coords[0]))

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

    def test_response_check_distances_signed_in_user_sending_params(self):
        """ This tests ask the feed without lat and lon and expects
        the lat and lon are retrieved from user model saved in db
        """

        # Create some locations
        location_madrid = Point(-3.8196228, 40.4378698)  # Madrid 0
        location_paris = Point(2.3488, 48.8534)  # Paris 1
        location_london = Point(-0.3817834, 51.528308)  # London 2
        location_berlin = Point(13.4105, 52.5244)  # Berlin 3
        location_rome = Point(12.395912, 41.909986)  # Rome 4

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

        # Generate a request search for "testing" key word
        request = self.factory.get(
            '/api/v1/service/feed?lat=%s&lon=%s' % (
                location_rome.coords[1],
                location_rome.coords[0]))

        # Attach the user to the request
        force_authenticate(request, user=self.users[3])

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
            ["4", "5", "2", "1", "3"]
        )

        # check the user location is updated
        self.users[3] = User.objects.get(id=self.users[3].id)
        self.assertEqual(location_rome.coords, self.users[3].location.coords)

    def test_sending_params_and_not_updating_user_location(self):
        """ This tests ask the feed without lat and lon and expects
        the lat and lon are retrieved from user model saved in db
        """

        # Create some locations
        location_madrid = Point(-3.8196228, 40.4378698)  # Madrid 0
        location_paris = Point(2.3488, 48.8534)  # Paris 1
        location_london = Point(-0.3817834, 51.528308)  # London 2
        location_berlin = Point(13.4105, 52.5244)  # Berlin 3
        location_rome = Point(12.395912, 41.909986)  # Rome 4

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

        # Make like the user set her location manually
        self.users[3].location_manually_set = True
        self.users[3].save()

        # Generate a request search for "testing" key word
        request = self.factory.get(
            '/api/v1/service/feed?lat=%s&lon=%s' % (
                location_rome.coords[1],
                location_rome.coords[0]))

        # Attach the user to the request
        force_authenticate(request, user=self.users[3])

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
            ['5', '2', '4', '1', '3']
        )

        # Check the user location is not updated
        self.users[3] = User.objects.get(id=self.users[3].id)
        self.assertEqual(location_berlin.coords, self.users[3].location.coords)

    def test_category_filtering(self):
        Service.objects.all().update(category=Category.objects.first())
        serv = Service.objects.first()
        serv.category = Category.objects.last()
        cat = Category.objects.last()
        serv.save()
        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?category='+str(cat.id))
        # Attach the user to the request
        force_authenticate(request, user=self.users[3])

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

    def test_wrong_category(self):
        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?category=2000000')
        # Attach the user to the request
        force_authenticate(request, user=self.users[3])

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

    def test_text_search_filtering(self):
        Service.objects.all().update(category=Category.objects.first())
        serv = Service.objects.first()
        serv.title = 'wordtobesearched'
        serv.save()
        # Generate a request search for "testing" key word
        request = self.factory.get('/api/v1/service/feed?search=wordtobesearched')
        # Attach the user to the request
        force_authenticate(request, user=self.users[3])

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


class TestServiceDetail(BaseServiceTestCase):

    # def tearDown(self):
    #    Category.objects.all().delete()

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestServiceDetail, self).setUp()

        location_madrid = Point(-3.8196228, 40.4378698)  # Madrid 0
        location_paris = Point(2.3488, 48.8534)  # Paris 1

        # Create self.users, Services & Categories for test cases
        self.user = UserFactory(location=location_madrid)
        self.owner = UserFactory(location=location_paris)
        self.service = ServiceFactory(
            category=Category.objects.first(),
            author=self.owner,
            title='1',
        )

    def test_service_detail_get_with_distance(self):
        Service.objects.all().update(category=Category.objects.first())
        serv = Service.objects.first()

        factory = APIRequestFactory()
        request = factory.get('/api/v1/service/{0}/'.format(serv.uuid))
        view = ServiceDetail.as_view()
        force_authenticate(request, user=self.user)
        response = view(request, uuid=serv.uuid)
        self.assertEqual(
            response.data['uuid'],
            str(serv.uuid)
        )

        self.assertEqual(
            response.data['distance'],
            1043.4
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_service_detail_get_anonymous_user(self):
        Service.objects.all().update(category=Category.objects.first())
        serv = Service.objects.first()

        response = self.client.get('/api/v1/service/{0}/'.format(serv.uuid))
        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.data['uuid'],
            str(serv.uuid)
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_service_detail_with_no_photos(self):
        serv = ServiceFactory(
            category=Category.objects.first(),
            author=self.owner,
            title='1',
        )
        serv.photos.all().delete()

        photos = ServiceSerializer(serv).data['photos']
        self.assertEqual(
            photos[0]['photo'],
            '/media/' + settings.SERVICE_PLACEHOLDER_PHOTO
        )


class TestUserServicesList(BaseServiceTestCase):

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestUserServicesList, self).setUp()

        # Instantiate the view directly. Never do this outside a test!
        self.view = UserServiceList.as_view()

        # Create self.users, Services & Categories for test cases
        self.users = UserFactory.create_batch(size=2)
        self.services = ServiceFactory.create_batch(
            size=2,
            category=Category.objects.first()
        )

        # Assign each service to 1 of the self.users
        self.services[0].author = self.users[0]
        self.services[0].title = "0"
        self.services[0].description = "testing"
        self.services[0].save()
        self.services[1].author = self.users[1]
        self.services[1].title = "1"
        self.services[1].description = "testing"
        self.services[1].save()

    def test_user_services(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word
        response = self.client.get(reverse('api_users:list', kwargs={'user_uuid': str(self.users[0].uuid)}))

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
            ["0"]
        )

    def test_user_services_empty(self):
        """ This tests ask for all the services of a user
        """
        # Generate a request search for "testing" key word
        self.users[0].services.all().delete()
        response = self.client.get(reverse('api_users:list', kwargs={'user_uuid': str(self.users[0].uuid)}))

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
            []
        )
