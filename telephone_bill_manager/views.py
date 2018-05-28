#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import TelephoneBill
from .serializers import TelephoneBillSerializer


class TelephoneBill(generics.ListAPIView):

    def get_queryset(self):
        queryset = get_object_or_404(TelephoneBill, subscriber=self.kwargs['subscriber'])
        serializer_class = TelephoneBillSerializer
