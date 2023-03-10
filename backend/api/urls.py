from django.urls import include, path, re_path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CarViewSet, CommentViewSet, CountryViewSet

router = DefaultRouter()
router.register(r'countrys', CountryViewSet, basename='country')
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'cars/(?P<car_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('/swagger-ui/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
