from pytest_django.asserts import assertTemplateUsed


def test_home_page_view(client):
    response = client.get("")
    assertTemplateUsed(response, "index.html")
    assertTemplateUsed(response, "base.html")
