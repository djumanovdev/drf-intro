from django.urls import path
from .views import ItemsViewSet


urlpatterns = [
    path('items/', ItemsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('items/<int:pk>/', ItemsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
