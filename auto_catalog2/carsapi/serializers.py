from rest_framework import serializers
from .models import Car


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rating')


class CarPopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'rating')


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rating')


class CarCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        Fields = ('make', 'model')
