from rest_framework import serializers

from semillas_backend.users.serializers import UserSerializer

from .models import Wallet, Transaction

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
            self.context['owner_uuid'] == obj.wallet_source.owner.uuid
        ):
            return obj.wallet_dest.owner.name
        return obj.wallet_source.owner.name

    def get_balance(self, obj):
        if type(self.context['view']).__name__ ==  "UserWalletDetail":
            owner_uuid = self.context['view'].kwargs['owner_uuid']
            is_owner = bool(owner_uuid == str(obj.wallet_source.owner.uuid))
            # import ipdb;ipdb.set_trace()
            if is_owner:
                return obj.balance_source
            else:
                return obj.balance_dest
        else:
            return obj.balance_source

    def get_trans_value(self, obj):
        if type(self.context['view']).__name__ ==  "UserWalletDetail":
            owner_uuid = self.context['view'].kwargs['owner_uuid']
            is_owner = bool(owner_uuid == str(obj.wallet_source.owner.uuid))
            if is_owner:
                return -obj.value
            else:
                return obj.value
        else:
            return obj.value

class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    owner = UserSerializer()
    class Meta:
        model = Wallet
        fields = ('uuid', 'owner', 'balance', 'last_updated', 'transactions')
