import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_root():
    client = APIClient()
    response = client.get("/")

    # Should return 302 since it redirects to the head API URL (see base.py)
    assert response.status_code == 302

    # Ensure the response contains a redirect location
    assert "Location" in response