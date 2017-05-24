from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    location = PointField()

    class Meta:
        model = User
        fields = ('uuid', 'name', 'picture', 'location', 'username', 'last_login')


from wallet.serializers import WalletSerializer
class FullUserSerializer(UserSerializer):

    wallet = WalletSerializer()

    class Meta:
        model = User
        fields = ('uuid', 'name', 'picture', 'location', 'username', 'last_login', 'wallet', 'email')
