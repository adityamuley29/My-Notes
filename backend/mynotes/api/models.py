from django.db import models
from accounts.models import User
# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    createdBy = models.CharField(max_length=300 ,default=None)

    def __str__(self):
        return self.body[0:50]
