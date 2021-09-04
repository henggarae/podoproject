from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import include_rank

class User(AbstractUser):
    name = models.CharField(
        max_length=6,
        unique=False,
        null=True,
    )
    rank = models.CharField(
        max_length=2,
        unique=False,
        null=True,
        validators=[include_rank],
    )

    def __str__(self):
        return self.username
    
class Post(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    platoon_member = models.CharField(max_length=10)
    platoon_member_rank = models.CharField(max_length=2,unique=False,null=True,validators=[include_rank])
    content = models.TextField(null=True)
    
    
    
    
    def __str__(self):
        return self.platoon_member
    