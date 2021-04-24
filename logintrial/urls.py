from django.urls import path, include
from rest_framework import routers
from logintrial.views import UserView


router = routers.DefaultRouter()
router.register(prefix='users', viewset=UserView, basename='users')

urlpatterns = [
    path('', include(router.urls), name='api'),
]