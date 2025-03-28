import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user("test123", "user@example.com")
    assert user.pk
    assert user.email == "user@example.com"
    assert not user.is_staff
    assert not user.is_superuser
