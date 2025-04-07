import pytest


@pytest.fixture(scope="function")
def create_user(django_user_model):
    return (
        django_user_model.objects.create_user(username="Lovecreft", password="123456"),
    )


@pytest.fixture(scope="session")
def create_profile():
    def _create_profile(user, **kwargs):
        user = user
        favorite_city = kwargs.get("favorite_city", "Providence")

    return _create_profile
