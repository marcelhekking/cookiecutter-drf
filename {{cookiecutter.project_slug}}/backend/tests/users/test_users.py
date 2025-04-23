import pytest
from rest_framework.test import APIClient

from tests.factories.users import UserFactory
from {{cookiecutter.project_slug}}.users.models import User


@pytest.fixture
def api_client(client):
    """Fixture to provide an API client."""
    return APIClient()


@pytest.mark.django_db
def test_api_get(api_client):
    """Test getting a list of users via the `users` API."""
    user = UserFactory(first_name="olduser")
    response = api_client.get("/api/v1/users/")
    assert response.status_code == 200
    assert response.data == {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        ],
    }


@pytest.mark.django_db
def test_api_post(api_client):
    """Test posting to the `users` API.

    This test creates a new user by posting to the `users` API and checks if the
    user is created. Any user is allowed to create a new user.
    """
    payload = {
        "username": "newuser",
        "password": "newpassword",
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User",
    }
    response = api_client.post("/api/v1/users/", data=payload)
    assert response.status_code == 201
    assert response.data["username"] == "newuser"
    assert response.data["email"] == "newuser@example.com"


@pytest.mark.django_db
def test_api_put_allowed(api_client):
    """Test updating a user via the API.

    Updating a user can only be done by the user itself. So this test passes.
    """
    user = UserFactory(first_name="olduser")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    payload = {
        "first_name": "Updated",
    }
    response = api_client.put(f"/api/v1/users/{user.id}/", data=payload)
    assert response.status_code == 200
    changed_user = User.objects.get(id=user.id)
    assert changed_user.first_name == "Updated"


@pytest.mark.django_db
def test_api_put_not_allowed(api_client):
    """Test updating a user via the API.

    Updating a user can only be done by the user itself. So this test must fail.
    """
    user = UserFactory()
    otheruser = UserFactory(first_name="olduser")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    payload = {
        "first_name": "Updated",
    }
    response = api_client.put(f"/api/v1/users/{otheruser.id}/", data=payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_api_patch_allowed(api_client):
    """Test patching a user via the `users` API.

    Updating a user can only be done by the user itself. So this test passes.
    """
    user = UserFactory(first_name="olduser")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    payload = {
        "first_name": "Updated",
    }
    response = api_client.patch(f"/api/v1/users/{user.id}/", data=payload)
    assert response.status_code == 200
    changed_user = User.objects.get(id=user.id)
    assert changed_user.first_name == "Updated"


@pytest.mark.django_db
def test_api_patch_not_allowed(api_client):
    """Test patching a user via the `users` API.

    Patching a user can only be done by the user itself. So this test must fail.
    """
    user = UserFactory()
    otheruser = UserFactory(first_name="olduser")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    payload = {
        "first_name": "Updated",
    }
    response = api_client.patch(f"/api/v1/users/{otheruser.id}/", data=payload)
    assert response.status_code == 403
