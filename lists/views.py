from .models import ToDoItem
from .serializers import ToDoItemSerializer
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# class IndexViewSet(viewsets.ModelViewSet):
#     queryset = ToDoItem.objects.all()
#     serializer_class = ToDoItemSerializer


@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def todo_list(request, pk=None):
    if request.method == 'GET':
        if pk:
            todo = ToDoItem.objects.get(pk=pk).__dict__
            todo.pop('_state', None)
            return JsonResponse(todo, safe=False)
        else:
            todos = ToDoItem.objects.values()
            return JsonResponse(list(todos), safe=False)

    elif request.method == 'POST':
        try:
            todo = request.data.dict()
            if todo.get('date', None):
                todo['date'] = datetime.strptime(todo['date'], '%d/%m/%Y').date()
            test = ToDoItem(**todo)
            test.save()
            test.__dict__.pop('_state', None)
            return JsonResponse(test.__dict__)
        except ValueError:
            return Response({"date":"Date format should be in DD-MM-YYYY"}, status.HTTP_400_BAD_REQUEST)

    elif pk:
        try:
            todo = ToDoItem.objects.get(pk=pk)
        except ToDoItem.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            todo.delete()
            return Response(status.HTTP_204_NO_CONTENT)

        elif request.method == 'PATCH':
            update_value = request.data.dict()
            if update_value['done'] == 'true':
                todo.done=True
                todo.save()
                return Response(status.HTTP_204_NO_CONTENT)
            return Response(status.HTTP_400_BAD_REQUEST)




