from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Container(models.Model):
  container_id = models.CharField(max_length=1000, unique=True)
  access_key = models.CharField(max_length=1000, unique=True, null=True)
  secret_key = models.CharField(max_length=1000, unique=True, null=True)
  ip_address = models.CharField(max_length=1000, null=True)
  port = models.CharField(max_length=1000, null=True)

  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    null=True
  )

  def __str__(self):
    return self.container_id


class Command(models.Model):
  command_id = models.CharField(max_length=1000, unique=True)
  access_key = models.CharField(max_length=1000, unique=True, null=True)
  secret_key = models.CharField(max_length=1000, unique=True, null=True)
  ip_address = models.CharField(max_length=1000, null=True)
  port = models.CharField(max_length=1000, null=True)

  sender = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="sender"
  )

  def __str__(self):
    return self.command_id
