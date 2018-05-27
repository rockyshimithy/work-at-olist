#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import generics

from .models import TelephoneBill
from .serializers import TelephoneBillSerializer


class TelephoneBill(generics.RetrieveAPIView):

    queryset = TelephoneBill.objects.all()
    serializer_class = TelephoneBillSerializer
    name = 'telephone_bill_retrieve'
