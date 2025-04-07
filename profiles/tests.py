import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view_use_index_template(client):
    url = reverse("profiles:index")
    response = client.get(url)
    assertTemplateUsed(response, "profiles/index.html")
