from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    class Meta:
        model = User
        fields = ('id', 'name', 'picture', 'location', 'email', 'username', 'last_login')
