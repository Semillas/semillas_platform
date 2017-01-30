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
		# import ipdb;ipdb.set_trace()
		# is_owner = bool(self.context['wallet'].owner == obj.wallet_source.owner)
		# if is_owner:
		return obj.wallet_dest.owner.name
		# else:
		#     return obj.wallet_source.owner.name

	def get_balance(self, obj):
		# import ipdb;ipdb.set_trace()
		# is_owner = bool(self.context['wallet'].owner == obj.wallet_source.owner)
		# if is_owner:
		return obj.balance_source
		# else:
		#     return obj.balance_dest

class WalletSerializer(CreateWalletSerializer):
	""" Usage:
	    from rest_framework.renderers import JSONRenderer
	    from semillas_backend.users.serializers import UserSerializer

	    JSONRenderer().render(UserSerializer(user_instance).data)
	"""
	transactions = TransactionSerializer(many=True)
	owner = UserSerializer()