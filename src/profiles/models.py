from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    A class to represent a user's profile

    ...

    Attributes
    ----------
    user: User
        the user linked to the profile
    favorite_city: str
        the user's favorite city
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        return str(self.user.username)
