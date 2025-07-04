from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand

from {{cookiecutter.project_slug}}.users.models import User


class Command(BaseCommand):
    def handle(self, *args: Any, **options: dict[str, Any]) -> None:
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(" ", "")
                email = user[1]
                password = "OnlyValidLocally"
                self.stdout.write("Creating account for %s (%s)" % (username, email))
                admin = User.objects.create_superuser(
                    email=email, username=username, password=password
                )
                admin.is_active = True
                admin.is_superuser = True
                admin.save()
        else:
            self.stdout.write(
                "Admin accounts can only be initialized if no Accounts exist"
            )
