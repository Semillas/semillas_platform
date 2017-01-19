from django.test import RequestFactory

from test_plus.test import TestCase

from ..views import FeedServiceList

from django.contrib.gis.geos import Point

from semillas_backend.users.factory import UserFactory
from wallet.factory import WalletFactory

from wallet.models import Wallet


class BaseWalletTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()



