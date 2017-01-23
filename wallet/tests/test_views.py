from django.test import RequestFactory

from test_plus.test import TestCase

from django.contrib.gis.geos import Point

from semillas_backend.users.factory import UserFactory
from wallet.factory import WalletFactory
from wallet.models import Wallet
import ipdb


class BaseWalletTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()




	




