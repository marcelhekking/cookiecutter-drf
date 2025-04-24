import pytest
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from tests.factories.users import UserFactory


@pytest.mark.django_db
def test_get_new_token():
    """Test new token creation."""
    client = APIClient()
    url = reverse("get-token")

    # Test that GET requests are not allowed
    response = client.get(url)
    assert response.status_code == 405

    # Create a user and test token generation
    user = UserFactory(username="test", password="a_password")
    user.set_password("a_password")
    user.save()
    user.auth_token.delete()
    assert user.auth_token.key is None

    # Create a new token for the user by posting the same credentials to the
    # get-token endpoint
    response = client.post(url, data={"username": "test", "password": "a_password"})
    assert response.status_code == 200
    token = response.json()["token"]
    assert Token.objects.get(user=user).key == token


@pytest.mark.django_db
def test_get_existing_token():
    """Test existing token retrieval."""
    client = APIClient()
    url = reverse("get-token")

    # Test that GET requests are not allowed
    response = client.get(url)
    assert response.status_code == 405

    # Create a user and test existinfg token retrieval
    user = UserFactory(username="test", password="a_password")
    user.set_password("a_password")
    user.save()
    assert user.auth_token.key is not None

    # Get the existing token for the user by posting the same credentials to the
    # get-token endpoint
    response = client.post(url, data={"username": "test", "password": "a_password"})
    assert response.status_code == 200
    token = response.json()["token"]
    assert Token.objects.get(user=user).key == token
