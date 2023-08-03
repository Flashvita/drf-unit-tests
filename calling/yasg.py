from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


description= ""

schema_view = get_schema_view(
   openapi.Info(
      title="Api Documentations for Calling ",
      default_version='v.1.1.1',
     
      description = description,
      license=openapi.License(name="BSD License"),
   ),  
   public=True,
   permission_classes=(permissions.AllowAny,),)

urlpatterns = [
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
