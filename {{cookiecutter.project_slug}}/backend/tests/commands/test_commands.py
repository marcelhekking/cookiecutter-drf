from io import StringIO

import pytest
from django.core.management import call_command as django_call_command

from {{cookiecutter.project_slug}}.users.models import User


def call_command(*args, **kwargs):
    out = StringIO()
    django_call_command(
        "initadmin",
        *args,
        stdout=out,
        stderr=StringIO(),
        **kwargs,
    )
    return out.getvalue()


@pytest.mark.django_db
def test_create_admin(settings):
    """Test creating admin user with `initadmin`."""
    settings.ADMINS = [("test", "test@test.com")]
    assert User.objects.count() == 0
    out = call_command()
    assert "Creating account for test (test@test.com)" in out
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_create_admin_when_user_already_exists():
    """Test `initadmin` when admin user already exists."""
    User.objects.create(username="admin", is_staff=True, is_superuser=True)
    assert User.objects.count() == 1
    out = call_command()
    assert "Admin accounts can only be initialized if no Accounts exist" in out
    assert User.objects.count() == 1
