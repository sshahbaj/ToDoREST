from rest_framework import viewsets
from .models import ToDoItem
from .serializers import ToDoItemSerializer


class IndexViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer