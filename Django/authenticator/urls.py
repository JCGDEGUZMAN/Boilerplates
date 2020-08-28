from django.urls import path
from django.conf.urls import url, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),
]