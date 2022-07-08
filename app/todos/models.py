# Create your models here.
from django.db import models

import jwt

from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models

from todoProj.settings import AUTH_USER_MODEL

class Todo(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    prior = models.CharField(max_length=10,blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    done_date = models.DateTimeField(blank=True, null=True)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title