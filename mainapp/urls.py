from xml.etree.ElementInclude import include
from django.urls import path, include
from mainapp import views


urlpatterns = [

    path('company/', views.CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='company'),
    path('company/<int:pk>/', views.CompanyViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='company_detail'),
]