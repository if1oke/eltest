from rest_framework import serializers

from car.models import Brand, Car, CarTTX, Comment, Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', 'country']


class CarTTXSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarTTX
        fields = ['id', 'car', 'door', 'engine', 'cylinder', 'kpp']

class CarSerializer(serializers.ModelSerializer):
    carttx = CarTTXSerializer()

    class Meta:
        model = Car
        fields = ['id', 'brand', 'carttx', 'year_release', 'year_completion',
                  'base_price', 'avg_price']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'email', 'car', 'pub_date', 'text']
