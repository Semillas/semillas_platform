from django.test import RequestFactory
from django.test import Client

from test_plus.test import TestCase

from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from semillas_backend.users.factory import UserFactory
from wallet.factory import TransactionFactory

from wallet import views

class BaseWalletTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
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

        request = self.factory.get('/api/v1/wallet/owner/')
        force_authenticate(request, user=self.user1)
        response = views.UserWalletDetail.as_view()(request, owner_uuid=self.user1.uuid)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )

    def test_create_transaction_ok(self):

        request = self.factory.post(
            '/api/v1/wallet/transactions/create/',
            {'user_source': self.user1.uuid,
            'user_dest': self.user2.uuid,
            'value': 5}
        )

        force_authenticate(request, user=self.user1)

        response = views.CreateTransaction.as_view()(request)

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

        # Request de wallet and check the transaction is created
        request = self.factory.get('/api/v1/wallet/owner/')
        force_authenticate(request, user=self.user1)
        response = views.UserWalletDetail.as_view()(request, owner_uuid=self.user1.uuid)
        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response.data['transactions'][0]['user'],
            self.user1.name
        )

    def test_create_transaction_without_balance(self):
        request = self.factory.post(
            '/api/v1/wallet/transactions/create/',
            {'user_source': self.user1.uuid,
            'user_dest': self.user2.uuid,
            'value': 25}
        )

        force_authenticate(request, user=self.user1)

        response = views.CreateTransaction.as_view()(request)

        self.assertEqual(
            response.status_code,
            400
        )

    def test_create_transaction_to_ourself(self):
        # Same wallet on source and destination
        request = self.factory.post(
            '/api/v1/wallet/transactions/create/',
            {'user_source': self.user1.uuid,
            'user_dest': self.user1.uuid,
            'value': 1}
        )

        force_authenticate(request, user=self.user1)

        response = views.CreateTransaction.as_view()(request)

        self.assertEqual(
            response.status_code,
            400
        )

    def test_create_transaction_from_others_wallet(self):
        # Same wallet on source and destination
        request = self.factory.post(
            '/api/v1/wallet/transactions/create/',
            {'user_source': self.user1.uuid,
            'user_dest': self.user2.uuid,
            'value': 1}
        )

        force_authenticate(request, user=self.user2)

        response = views.CreateTransaction.as_view()(request)

        # Expect: expect queryset of services ordered by proximity
        #   self.make_user()
        self.assertEqual(
            response.status_code,
            401
        )
