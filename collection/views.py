# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class CollectionIndexView(TemplateView):
    template_name = "index.html"
