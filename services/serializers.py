from rest_framework import serializers

from .models import Service, Category, ServicePhoto
from semillas_backend.users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'photo', 'order')

class ServicePhotoSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = ServicePhoto
        fields = ('id', 'photo')

class CreateServiceSerializer(serializers.ModelSerializer):
    """ Usage:
    """
    class Meta:
        model = Service
        fields = ('uuid', 'title', 'date', 'description', 'author', 'category', 'photos', 'seeds_price')

class ServiceSerializer(serializers.Serializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    category = CategorySerializer()
    photos = ServicePhotoSerializer(many=True)
    author = UserSerializer()
    lat = serializers.SerializerMethodField()
    lon = serializers.SerializerMethodField()
    # distance = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('uuid', 'title', 'date', 'description', 'author', 'category', 'photos', 'seeds_price', 'lat', 'lon', 'distance')

    def get_lat(self, obj):
        return obj.author.location.y

    def get_lon(self, obj):
        return obj.author.location.x

    def get_distance(self, obj):
        if hasattr(obj, 'dist'):
            return round(obj.dist.km,1)
        else:
            return None

