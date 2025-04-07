import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view_use_index_template(client):
    url = reverse("lettings:index")
    response = client.get(url)
    print(response)
    assertTemplateUsed(response, "lettings/index.html")
