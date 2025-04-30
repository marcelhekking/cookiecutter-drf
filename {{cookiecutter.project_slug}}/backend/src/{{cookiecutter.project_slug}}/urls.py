"""{{cookiecutter.project_slug}} URL Configuration"""

from typing import List, Union

from django.conf import settings
from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

from {{cookiecutter.project_slug}}.users.views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("get-token/", ObtainAuthToken.as_view(), name="get-token"),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve debug toolbar when not in testing mode
    if not settings.TESTING:
        from debug_toolbar.toolbar import debug_toolbar_urls
        urlpatterns += debug_toolbar_urls()
