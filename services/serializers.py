from datetime import datetime
from rest_framework import serializers
from rest_framework import fields

from django.conf import settings

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

class ServiceSerializer(serializers.ModelSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    category = CategorySerializer()
    photos = serializers.SerializerMethodField('get_photos_list')
    author = UserSerializer()
    lat = serializers.SerializerMethodField()
    lon = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('uuid', 'title', 'date', 'description', 'author', 'category', 'photos', 'seeds_price', 'lat', 'lon', 'distance')

    def get_photos_list(self, instance):
        photos = ServicePhoto.objects\
            .filter(service__id=instance.id)\
            .order_by('date')
        if not photos:
            photos = [ServicePhoto(
                date=datetime.now(),
                photo=settings.SERVICE_PLACEHOLDER_PHOTO
                )]
        return ServicePhotoSerializer(photos, many=True).data

    def get_lat(self, obj):
        return getattr(obj.author.location, 'y', 0)

    def get_lon(self, obj):
        return getattr(obj.author.location, 'x', 0)

    def get_distance(self, obj):
        if hasattr(obj, 'dist') and (obj.dist != None):
            distance = obj.dist.km
            return round(distance, 1)
        elif (not hasattr(obj, 'dist')) \
                and 'request' in self.context \
                and hasattr(self.context['request'].user, 'location') \
                and hasattr(obj.author, 'location'):
            distance = obj.author.location.distance(self.context['request'].user.location) * 100
            return round(distance,1)
        return None

class ServicePhotoUploadSerializer(serializers.ModelSerializer):
    """
    """
    updated_service = ServiceSerializer(read_only=True, source='service')
    class Meta:
        model = ServicePhoto
        fields = ('photo', 'service', 'updated_service')


class CreateServiceSerializer(serializers.ModelSerializer):
    """ Usage:
    """

    service = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            'uuid',
            'title',
            'description',
            'category',
            'seeds_price',
            'service'
        )

    def create(self, validated_data):
        service = Service(author=self.context['request'].user, **validated_data)
        service.save()
        return service

    def get_service(self, obj):
        return ServiceSerializer(obj).data


class UpdateServiceSerializer(CreateServiceSerializer):
    """ Usage:
    """

    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    seeds_price = serializers.IntegerField(required=False)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False
    )

