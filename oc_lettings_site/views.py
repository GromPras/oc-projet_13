from django.http.response import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    """
    Returns the home page
    """

    return render(request, "index.html")
