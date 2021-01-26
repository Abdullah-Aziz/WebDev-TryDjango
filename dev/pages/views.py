from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_views(request, *args, **kwargs):
    return render(request, 'home.html', {})


def about_views(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [1,2,3,4]
    }
    return render(request, 'about.html', my_context)


def contact_views(request, *args, **kwargs):
    return render(request, 'contact.html', {})
