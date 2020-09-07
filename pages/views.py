from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # request.user = username
    return render(request, "home.html", {
        "my_text": "This is about me",
        "my_number": "01987654320",
        "my_list": [123, 456, 789]
    })
