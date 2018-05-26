#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from .views import TelephoneCall

app_name = 'call_manager'

urlpatterns = [
    path('', TelephoneCall.as_view(), name=TelephoneCall.name),
]
