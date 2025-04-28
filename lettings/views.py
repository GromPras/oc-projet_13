from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Letting


def index(request) -> HttpResponse:
    """
    Return a list of lettings
    """

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id: int) -> HttpResponse:
    """
    Return a single letting

    Parameters:
        letting_id (int): The letting id
    """

    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
