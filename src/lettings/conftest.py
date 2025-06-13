import pytest

from lettings.models import Address, Letting


@pytest.fixture(scope="session")
def create_letting():
    def _create_letting(address, **kwargs):
        return Letting.objects.create(
            title=kwargs.get("title", "Test letting"), address=address
        )

    return _create_letting


@pytest.fixture(scope="session")
def create_address():
    def _create_letting(**kwargs):
        return Address.objects.create(
            number=kwargs.get("number", "10"),
            street=kwargs.get("street", "Barnes Street"),
            city=kwargs.get("city", "Providence"),
            state=kwargs.get("state", "Rhode Island"),
            zip_code=kwargs.get("zip_code", "02906"),
            country_iso_code=kwargs.get("country_iso_code", "USA"),
        )

    return _create_letting
