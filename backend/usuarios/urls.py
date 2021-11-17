from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from usuarios.api import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
