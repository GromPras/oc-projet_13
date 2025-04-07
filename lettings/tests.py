import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view_use_index_template(client):
    url = reverse("lettings:index")
    response = client.get(url)
    assertTemplateUsed(response, "lettings/index.html")
    assertTemplateUsed(response, "base.html")


@pytest.mark.django_db
def test_letting_is_shown(client, create_address, create_letting):
    address = create_address()
    letting = create_letting(address, title="Lovecraft's House")
    url = reverse("lettings:detail", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
    assertTemplateUsed(response, "base.html")
    assert response.context["title"] == letting.title
    assert response.context["address"] == address
