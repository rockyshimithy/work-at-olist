#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from .views import TelephoneBill

app_name = 'telephone_bill_manager'

urlpatterns = [
    path('', TelephoneBill.as_view(), name=TelephoneBill.name),
]
