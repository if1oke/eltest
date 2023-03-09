from rest_framework import viewsets

from .serializers import (BrandSerializer, CarSerializer,
                                     CarTTXSerializer, CommentSerializer,
                                     CountrySerializer)
from car.models import Brand, Car, CarTTX, Comment, Country


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarTTXViewSet(viewsets.ModelViewSet):
    queryset = CarTTX
    serializer_class = CarTTXSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
