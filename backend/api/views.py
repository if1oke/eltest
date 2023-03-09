from rest_framework import viewsets

from backend.car.models import Country


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    pass


class BrandViewSet(viewsets.ModelViewSet):
    pass


class CarViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass
