from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    first_name = None
    last_name = None
    
    class Meta:
        db_table = 'user'