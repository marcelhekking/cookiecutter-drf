from django.urls import reverse
from django_webtest import WebTest
from rest_framework.authtoken.models import Token
from tests.factories.users import UserFactory


def test_root(django_app):
    resp = django_app.get("/")

    # should return 302 since it redirects to the head API url (see base.py)
    assert resp.status_code == 302


class ObtainTokenTests(WebTest):
    """
    Test that the token url as JSON api works.
    """

    def test_json_renderer(self):
        """
        Assert that by default the JSON renderer is used.
        """
        url = reverse("get-token")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

        user = UserFactory.create(username="test", password="a_password")
        user.set_password("a_password")
        user.save()
        user.auth_token.delete()
        response = self.client.post(
            url, data={"username": "test", "password": "a_password"}
        )
        token = response.json()["token"]
        self.assertEqual(Token.objects.get(user=user).key, token)
