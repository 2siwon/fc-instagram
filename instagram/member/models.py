from django.contrib.auth.models import (
    AbstractUser,
    UserManager as DjangoUserManager
)
from django.db import models


class UserManager(DjangoUserManager):

    # createsuperuser 할 때 age를 물어보지않고 기본값 30
    def create_superuser(self, *args, **kwargs):
        super().create_superuser(age=30, *args, **kwargs)


class User(AbstractUser):
    img_profile = models.ImageField(
        upload_to='user',
        blank=True)

    age = models.IntegerField()

    objects = UserManager()

    # createsuperuser시에 반드시 물어봐야 할 필드
    # (기존 REQUIRED_FIELDS메소드에 age추가
    # REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['age']
