import pytest

from tests.factories.users import UserFactory


@pytest.mark.django_db
def test_create_user():
    user = UserFactory()
    assert user.pk
    assert not user.is_staff
    assert not user.is_superuser
