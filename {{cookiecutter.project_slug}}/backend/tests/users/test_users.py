import pytest
from rest_framework.test import APIClient

from tests.factories.users import UserFactory
from {{cookiecutter.project_slug}}.users.models import User


@pytest.fixture
def api_client(client):
    """Fixture to provide an API client."""
    return APIClient()


@pytest.fixture
def authenticated_api_client():
    """Fixture to provide an authenticated API client."""
    user = UserFactory()
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.mark.django_db
def test_api_get_authenticated(authenticated_api_client):
    """Test getting a list of users via the `users` API.

    Only if the user is authenticated, the API returns a list of users.
    """
    response = authenticated_api_client.get("/api/v1/users/")
    assert response.status_code == 200
    assert response.data["count"] == 1


@pytest.mark.django_db
def test_api_get_not_authenticated(api_client):
    """Test getting a list of users via the `users` API.

    No response is returned if the user is not authenticated.
    """
    response = api_client.get("/api/v1/users/")
    assert response.status_code == 403


@pytest.mark.django_db
def test_api_get(authenticated_api_client):
    """Test getting a list of users via the `users` API.

    Only if the user is authenticated, the API returns a list of users.
    """
    response = authenticated_api_client.get("/api/v1/users/")
    assert response.status_code == 200
    assert response.data["count"] == 1


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
    user = UserFactory(first_name="firstname", last_name="lastname")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    payload = {
        "first_name": "Updated",
    }
    response = api_client.put(f"/api/v1/users/{user.pk}/", data=payload)
    assert response.status_code == 200
    changed_user = User.objects.get(id=user.pk)
    assert changed_user.first_name == "Updated"
    # PUT behaves like PATCH, so the last name should not be changed
    assert changed_user.last_name == "lastname"


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
    response = api_client.put(f"/api/v1/users/{otheruser.pk}/", data=payload)
    assert response.status_code == 403

