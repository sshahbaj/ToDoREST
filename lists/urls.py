from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.IndexViewSet.as_view({'get': 'list', 'post': 'create'}), name='index-list'),
    path('<int:pk>/', views.IndexViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), name='index-destroy'),
]