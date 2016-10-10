from rest_framework import serializers

from .models import Service, Category, ServicePhoto


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


class ServiceSerializer(serializers.ModelSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    category = CategorySerializer()
    photos = ServicePhotoSerializer(many=True)
    class Meta:
        model = Service
        fields = ('id', 'title', 'date', 'description', 'category', 'photos')
