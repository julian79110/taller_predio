"""
URL configuration for predios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#django
from django.contrib import admin
from django.urls import path, include

#djangorestframework (creacion de api's)
from rest_framework import routers

#predio
from predio.api.views import UserViewSet, PredioViewSet, SubirJSONView, TipoPredioViewSet, PropietarioViewSet, TipoPropietarioViewSet, TipoNumeroDocumentoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'predios', PredioViewSet)
router.register(r'tipopredio', TipoPredioViewSet)
router.register(r'propietarios', PropietarioViewSet)
router.register(r'tipopropietario', TipoPropietarioViewSet)
router.register(r'tipodocumento', TipoNumeroDocumentoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predio.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/subir-archivo/', SubirJSONView.as_view(), name='subir-archivo')
]
