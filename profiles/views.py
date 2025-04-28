from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Profile


def index(request) -> HttpResponse:
    """
    Returns a list of profiles
    """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username: str) -> HttpResponse:
    """
    Returns a single profile

    Parameters:
        username (str): The user's username
    """

    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
