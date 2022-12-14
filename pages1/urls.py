#!/usr/bin/env python
__author__ = "Ryan Manella"

from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
