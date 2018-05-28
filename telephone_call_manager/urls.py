#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from .views import TelephoneCall

app_name = 'telephone_call_manager'

urlpatterns = [
    path('', TelephoneCall.as_view(), name='telephone_call_entry'),
]
