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

class ServiceSerializer(CreateServiceSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    category = CategorySerializer()
    photos = ServicePhotoSerializer(many=True)
    author = UserSerializer()
