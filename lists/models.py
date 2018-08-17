from django.db import models
import datetime


class ToDoItem(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    auto_increment_id = models.AutoField(primary_key=True, default=None)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
