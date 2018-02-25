from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from rest_auth.models import TokenModel
from .serializers import ProfileSerializer


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    user = ProfileSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user')
