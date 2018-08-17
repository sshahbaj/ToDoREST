from rest_framework import serializers
from .models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    class Meta:
        model = ToDoItem
        fields = ('subject', 'date', 'auto_increment_id', 'done')