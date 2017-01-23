from rest_framework import serializers

from .models import Wallet, Transaction
from semillas_backend.users.serializers import UserSerializer


class CreateWalletSerializer(serializers.ModelSerializer):
    """ Usage:
    """

    class Meta:
        model = Wallet
        fields = ('uuid', 'owner', 'balance', 'last_updated', 'transactions')

class TransactionSerializer(CreateWalletSerializer):
    user = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ('id', 'value', 'balance', 'user', 'created_at')

    def get_user(self, obj):
        # if (self.request.wallet == obj)
        return obj.wallet_dest.owner.name

    def get_balance(self, obj):
        # if (Wallet.objects.get(uuid=transactions.wallet) == obj.wallet_source):
        #     return obj.balance_source
        # else:
        #     return obj.balance_dest
        return obj.balance_source

class WalletSerializer(CreateWalletSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    transactions = TransactionSerializer(many=True)
    owner = UserSerializer()

