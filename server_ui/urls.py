# -*- coding: utf-8 -*-
from django.conf.urls import re_path

from .views import home, about, docs, faq, privacy
from . import views

urlpatterns = [
  re_path(r'^$', views.home),
  re_path(r'^about$', views.about),
  re_path(r'^docs$', views.docs),
  re_path(r'^faq$', views.faq),
  re_path(r'^privacy$', views.privacy),
]
