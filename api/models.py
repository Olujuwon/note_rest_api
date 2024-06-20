from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    shareable = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  #this should be  FK TO USER
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updatedAt']

    def __str__(self):
        return self
