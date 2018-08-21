from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.todo_list, name='index-list'),
    path('<int:pk>/', views.todo_list, name='index-detail'),
    path('done/', views.done_list, name='done-list'),
]