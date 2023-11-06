from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book


# Create your views here.
def resume(request):
    template = loader.get_template("resume.html")
    return HttpResponse(template.render())


def book(request):
    b1 = Book.objects.all()
    return render(request, "index.html", {"b1": b1})
