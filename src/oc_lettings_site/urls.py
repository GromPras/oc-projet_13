from django.contrib import admin
from django.urls import include, path

from . import views


def trigger_error(request):
    """
    Simple function to test Sentry integration
    Should be removed after validation
    """
    division_by_zero = 1 / 0  # noqa


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
