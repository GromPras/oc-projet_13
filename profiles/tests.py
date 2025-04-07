import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view_use_index_template(client):
    url = reverse("profiles:index")
    response = client.get(url)
    assertTemplateUsed(response, "profiles/index.html")


def test_profile_is_show(client, create_user, create_profile):
    user = create_user
    profile = create_profile(user)
    url = reverse("profiles:detail", args=[profile.user.username])
    response = client.get(url)
    assertTemplateUsed(response, "profiles/profile.html")
    assert response.context["profile"] == profile
