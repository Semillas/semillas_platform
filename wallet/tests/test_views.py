from django.test import RequestFactory
from django.test import Client

from test_plus.test import TestCase

from semillas_backend.users.factory import UserFactory
from wallet.factory import TransactionFactory

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
        response = c.get('/api/v1/wallet/owner/%s/' % self.user1.uuid)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )
    def test_create_transaction_ok(self):

        c = Client()
        c.force_login(self.user1)
        response = c.post('/api/v1/wallet/transactions/create/', {'wallet_source': self.user1.wallet.id, 'wallet_dest': self.user2.wallet.id, 'value': 5})
        self.user1.wallet.refresh_from_db()
        self.user2.wallet.refresh_from_db()

        self.assertEqual(
            response.status_code,
            201
        )

        self.assertEqual(
            self.user1.wallet.balance,
            5
        )

        self.assertEqual(
            self.user2.wallet.balance,
            15
        )
    def test_create_transaction_without_balance(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post('/api/v1/wallet/transactions/create/', {'wallet_source': self.user1.wallet.id, 'wallet_dest': self.user2.wallet.id, 'value': 25})
        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            400
        )

    def test_create_transaction_for_ourself(self):
        # Same wallet on source and destination
        c = Client()
        c.force_login(self.user1)
        response = c.post('/api/v1/wallet/transactions/create/', {'wallet_source': self.user1.wallet.id, 'wallet_dest': self.user1.wallet.id, 'value': 1})
        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            400
        )

