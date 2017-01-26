from django.test import RequestFactory

from test_plus.test import TestCase
from django.test import Client


from semillas_backend.users.factory import UserFactory
from wallet.factory import TransactionFactory
from wallet.models import Wallet

class BaseWalletTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        TransactionFactory(
            wallet_source=self.user1.wallet,
            wallet_dest=self.user2.wallet
        )



class WalletEndpointsTestCase(BaseWalletTestCase):

    def test_get_wallet(self):

        # Generate a request search for "testing" key word
        # Attach the user to the request
        c = Client()
        c.force_login(self.user1)
        response = c.get('/api/v1/wallet/%s/' % self.user1.uuid)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

        #self.assertIsInstance(
        #    response.data,
        #    list
        #)

        #self.assertEqual(
        #    [item["title"] for item in response.data],
        #    ["4", "2", "3", "5", "1"]
        #)







