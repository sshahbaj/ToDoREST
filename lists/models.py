from django.db import models
import datetime


class ToDoItem(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField(null=True)
    auto_increment_id = models.AutoField(primary_key=True, default=None)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Blog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    pub_date = models.DateField()