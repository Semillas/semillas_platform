from rest_framework import serializers

from semillas_backend.users.serializers import UserSerializer

from .models import Wallet, Transaction

class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('wallet_source', 'wallet_dest', 'value')

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    trans_value = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ('id', 'trans_value', 'balance', 'user', 'created_at')

    def get_user(self, obj):
        if (
            'owner_uuid' in self.context and
            self.context['owner_uuid'] == str(obj.wallet_source.owner.uuid)
        ):
            return obj.wallet_dest.owner.name
        return obj.wallet_source.owner.name

    def get_balance(self, obj):
        if (
            'owner_uuid' in self.context and
            self.context['owner_uuid'] == str(obj.wallet_source.owner.uuid)
        ):
            return obj.balance_source
        return obj.balance_dest

    def get_trans_value(self, obj):
        if (
            'owner_uuid' in self.context and
            self.context['owner_uuid'] == str(obj.wallet_source.owner.uuid)
        ):
            return -obj.value
        return obj.value

class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    owner = UserSerializer()
    class Meta:
        model = Wallet
        fields = ('uuid', 'owner', 'balance', 'last_updated', 'transactions')
