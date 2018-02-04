#from phonenumber_field.serializerfields import PhoneNumberField
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
        fields = ('uuid', 'name', 'picture', 'location', 'username', 'last_login',
                  'email', 'phone', 'faircoin_address', 'telegram_id')


class UpdateUserSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=False)
    #phone = PhoneNumberField(required=False)
    email = serializers.CharField(required=False)
    picture = serializers.ImageField(required=False)
    uuid = serializers.CharField(read_only=True)
    location = PointField(required=False)

    class Meta:
        model = User
        fields = ('name', 'picture', 'phone', 'email', 'uuid',
                  'faircoin_address', 'telegram_id', 'location',
                  'location_manually_set')


from wallet.serializers import WalletSerializer


class FullUserSerializer(UserSerializer):

    wallet = WalletSerializer()

    class Meta:
        model = User
        fields = ('uuid', 'name', 'picture', 'location', 'username', 'last_login', 'wallet', 'email', 'phone')
