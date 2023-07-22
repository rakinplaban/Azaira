from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    input_value = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)