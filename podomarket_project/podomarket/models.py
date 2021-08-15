from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import contains_special_character,no_special_character

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[no_special_character],
        error_messages={'unique':"이미 사용중인 닉네임"},
    )
    kakao_id = models.CharField(
        max_length=20,
        validators=[no_special_character],
        null=True,
    )
    address = models.CharField(
        max_length=40,
        null=True,
        validators=[no_special_character],

    )
    def __str__(self):
        return self.email


