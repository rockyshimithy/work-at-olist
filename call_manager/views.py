#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import generics

from .models import TelephoneCall
from .serializers import TelephoneCallSerializer


class TelephoneCall(generics.CreateAPIView):

    queryset = TelephoneCall.objects.all()
    serializer_class = TelephoneCallSerializer