from typing import Optional

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username: str

    def __str__(self) -> str:
        return self.usernam


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(
    sender: type[Model],
    instance: Optional[AbstractUser] = None,
    created: bool = False,
    **kwargs: dict,
) -> None:
    if created and instance is not None:
        Token.objects.create(user=instance)
