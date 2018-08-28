from django.db import models
from django.contrib.auth.models import User
import datetime


class ToDoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=False)
    subject = models.CharField(max_length=100)
    date = models.DateField(null=True)
    auto_increment_id = models.AutoField(primary_key=True, default=None)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
