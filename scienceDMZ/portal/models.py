from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Containers(models.Model):
  container_id = models.CharField(max_length=1000, unique=True)
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    null=True
  )
  def __str__(self):
    return self.container_id
