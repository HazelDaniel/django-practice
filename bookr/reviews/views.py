from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """view for the root route"""
    name = request.GET.get("name") or "World"
    return render(request, "base.html", context={"name": name})

def search(request):
    """view for the /search route"""
    resource = request.GET.get("search") or ""
    return render(request, "search.html", context={"search": resource})
