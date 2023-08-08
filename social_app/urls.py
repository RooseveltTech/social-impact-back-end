"""
URL configuration for social_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny

# Swagger-UI.
schema_view = get_schema_view(
    openapi.Info(
        title="MLSA SOCIAL IMPACT - GREEN AIR API ",
        default_version='v1',
        description="Django Backend API",
        terms_of_service="",
        contact=openapi.Contact(email="rooseveltabandy@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    url="https://backendgreenair.azurewebsites.net/",
    public=True,
    permission_classes=[AllowAny, ],
)
admin.site.site_header = "Green Air"
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('auth/', include('core.urls')),
    path('air/', include('air_quality_app.urls')),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
