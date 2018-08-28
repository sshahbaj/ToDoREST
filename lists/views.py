from .models import ToDoItem
from .serializers import ToDoItemSerializer
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.http import JsonResponse
import jwt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# class IndexViewSet(viewsets.ModelViewSet):
#     queryset = ToDoItem.objects.all()
#     serializer_class = ToDoItemSerializer

SECRET_KEY = 'Qwerty!@#'
ALGORITHM = 'HS256'


def invalid_token():
    return Response({'error': 'Invalid Token'}, status.HTTP_401_UNAUTHORIZED)


def get_token(request):
    try:
        return request.META['HTTP_AUTHORIZATION']
    except KeyError:
        return Response({'error': 'Token not found'}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def todo_list(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                jwt_token = request.META['HTTP_AUTHORIZATION']
            except (jwt.DecodeError, KeyError):
                return invalid_token()
            try:
                todo = ToDoItem.objects.get(pk=pk).__dict__
            except ObjectDoesNotExist:
                return Response({'auto_increment_id': pk, 'error': 'Task with this id does not exists'}, status.HTTP_404_NOT_FOUND)
            todo.pop('_state', None)
            return JsonResponse(todo, safe=False, status=200)
        else:
            try:
                jwt_token = request.META['HTTP_AUTHORIZATION']
                payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
                user = User.objects.get(id=payload['user_id'])
                todos = ToDoItem.objects.filter(user=user).exclude(done=True).order_by('date').values()
                return JsonResponse({'list': list(todos)}, safe=False, status=200)
            except (jwt.DecodeError, KeyError):
                return invalid_token()

    elif request.method == 'POST':
        try:
            jwt_token = request.META['HTTP_AUTHORIZATION']
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
            user = User.objects.get(id=payload['user_id'])
        except jwt.DecodeError:
            return invalid_token()
        try:
            todo = request.data
            if todo.get('date', None) and todo['date'] != '':
                todo['date'] = datetime.strptime(todo['date'], '%d/%m/%Y').date()
            else:
                todo['date'] = None
            todo['user'] = user
            test = ToDoItem(**todo)
            test.save()
            test.__dict__.pop('_state', None)
            return JsonResponse(test.__dict__, status=201)
        except ValueError:
            return Response({"date": "Date format should be in DD/MM/YYYY"}, status.HTTP_400_BAD_REQUEST)

    elif pk:
        try:
            jwt_token = request.META['HTTP_AUTHORIZATION']
        except (jwt.DecodeError, KeyError):
            return invalid_token()
        try:
            todo = ToDoItem.objects.get(pk=pk)
        except ToDoItem.DoesNotExist:
            return Response({'auto_increment_id': pk, 'error': 'Task with this id does not exists'}, status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            todo.delete()
            return Response(status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            update_value = request.data
            try:
                todo.subject = update_value['subject']
                if update_value.get('date', None) and update_value['date'] != '':
                    update_value['date'] = datetime.strptime(update_value['date'], '%d/%m/%Y').date()
                else:
                    update_value['date'] = None
                todo.date = update_value['date']
                todo.save()
                return Response(status.HTTP_204_NO_CONTENT)
            except Exception:
                return Response(status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PATCH':
            update_value = request.data
            if update_value['done'] is True:
                todo.done = True
                todo.save()
                return Response(status.HTTP_204_NO_CONTENT)
            return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def login(request):
    if request.data:
        post_data = request.data
    else:
        return Response({'error': 'Invalid Data'}, status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=post_data['username'])
        user.check_password(post_data['password'])
    except (User.DoesNotExist, User.PasswordDoesNotMatch):
        JsonResponse({'error': 'Wrong Credentials'}, status=400)

    payload = {
        'user_id': user.id
    }
    jwt_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return JsonResponse({'token': jwt_token.decode('utf-8'), 'username': user.username}, status=200)


@api_view(['POST'])
def signup(request):
    post_data = request.data
    username = post_data['username']
    password = post_data['password']
    try:
        user = User(username=username)
        user.set_password(password)
        user.save()
    except IntegrityError:
        return JsonResponse({'error': 'Username already taken'}, status=409)
    payload = {
        'user.id': user.id
    }
    jwt_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return JsonResponse({'token': jwt_token.decode('utf-8'), 'username': user.username}, status=201)


# @api_view(['GET', ])
# def done_list(request):
#     if request.method == 'GET':
#         done_todos = ToDoItem.objects.filter(done=True).order_by('date').values()
#         return JsonResponse({'list': list(done_todos)}, safe=True)




