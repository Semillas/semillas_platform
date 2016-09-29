from rest_framework import serializers
from .models import Wallet


class ServiceSerializer(serializers.ModelSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    class Meta:
        model = Wallet
        fields = ('user', 'seeds', 'created_at')
