#!/usr/bin/env python3
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """this is the view for the root route"""
    return HttpResponse("welcome to the root route")