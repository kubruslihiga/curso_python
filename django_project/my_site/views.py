from django.shortcuts import render, redirect
from .models import URLCoder


# Create your views here.
def index(request):
    urls = URLCoder.objects.filter()
    return render(request, "index.html", context={"urls": urls})


def save(request):
    url = request.GET.get("url")
    try:
        obj = URLCoder.objects.get(url=url)
    except URLCoder.DoesNotExist as e:
        obj = URLCoder(url=url)
    obj.save()
    return redirect(index)
