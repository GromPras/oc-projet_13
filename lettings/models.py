from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    A Class to represent an address

    ...

    Attributes
    ----------
    number: int
        the house number
    street: str
        the street name
    city: str
        the city name
    state: str
        the state name
    zip_code: int
        the zip_code
    country_iso_code: str
        the country iso code
    """

    class Meta:

        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self) -> str:
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    A class to represent a letting

    ...

    Attributes
    ----------
    title: str
        the title of the letting
    address: Address
        the related address for the letting
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)
